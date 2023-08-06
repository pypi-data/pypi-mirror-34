#
# Copyright (c) 2016 BlueData Software, Inc.
#

from __future__ import print_function
from .. import SubCommand
from ..constants import *
from ..inmem_store import ENTRY_DICT, DELIVERABLE_DICT

from ..utils import isDebug as isDebug
from ..utils import executeShellCmd as executeShellCmd
from ..utils.misc import getBaseOSMajorVersion, calculateMD5SUM
from ..utils.config import KEY_SDKBASE, KEY_STAGEDIR, KEY_DELIVERABLES, SECTION_WB

import os, gzip, stat, base64, shutil, hashlib, subprocess, json

DIRNAME = os.path.dirname(os.path.realpath(__file__))
BUNDLE_BUILD_DIR = os.path.abspath(os.path.join(DIRNAME, '..', 'appbuild'))
CATALOG_NAME_FMT = 'bdcatalog-%(ostype)s-%(sanitizeddistro)s-%(version)s'

CATALOG_EXTRACT_DIR = '/opt/bluedata/catalog/bundle/install'
LOGO_EXTRACT_DIR = '/opt/bluedata/catalog/bundle/logos'

class CatalogPackageV4(SubCommand):
    """

    """
    def __init__(self, config, inmemStore, cmdObj):
        SubCommand.__init__(self, config, inmemStore, cmdObj, 'package')

    def getSubcmdDescripton(self):
        return 'Package all components of the catalog into a bundle (.bin file).'

    def populateParserArgs(self, subparser):
        subparser.add_argument('-v', '--verbose', action='store_true',
                               dest='verbose', default=False,
                               help='Show details of the packing process.')

    def run(self, pargs):
        stageDir = self.config.get(SECTION_WB, KEY_STAGEDIR)
        delivDir = self.config.get(SECTION_WB, KEY_DELIVERABLES)

        if not os.path.exists(stageDir):
            os.makedirs(stageDir)

        delivDict = self.inmemStore.getDict(DELIVERABLE_DICT)
        entryDict = self.inmemStore.getDict(ENTRY_DICT)

        logoDict = entryDict.get('logo', {})
        imageDictList = delivDict.get('images', [])
        registryDict = entryDict.get('registry', {})
        appconfigDict = entryDict.get('setup_package', {})


        if len(imageDictList) == 0:
            print("ERROR: No container images are configured. Please use "
                  "'image build', 'image push' or 'image add' "
                  "with appropriate arguments.")
            return False

        distroId = entryDict['distro_id']
        sanitizedDistroId = distroId.replace('/', '-')
        catalogStagingDir = os.path.join(stageDir, sanitizedDistroId)

        imageOsTypes = []
        if len(imageDictList) > 0:
            for image in imageDictList:
                ostype = image['imageOS'] + image['imageOSMajor']
                if ostype not in imageOsTypes:
                    imageOsTypes.append(ostype)

        bundleOsType = imageOsTypes[0]
        if len(imageOsTypes) > 1:
            bundleOsType = "multipleos"

        bundleName = CATALOG_NAME_FMT % {'ostype'         : bundleOsType,
                                         'version'        : entryDict['version'],
                                         'sanitizeddistro': sanitizedDistroId}
        catalogBaseDir = os.path.join(catalogStagingDir, bundleName)

        if os.path.exists(catalogStagingDir):
            shutil.rmtree(catalogStagingDir)

        os.makedirs(catalogBaseDir)

        # Entry JSON file.
        if delivDict.has_key('entry'):
            entry = delivDict['entry'] # the json file.
            entryFileName = os.path.basename(entry)
            entryDestFile = os.path.join(catalogBaseDir, entryFileName)

            if isDebug():
                print("DEBUG: Copying %s to %s" % (entry, entryDestFile))

            shutil.copyfile(entry, entryDestFile)
            os.chmod(entryDestFile, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
        else:
            print("ERROR: 'catalog save' must be executed before packaging.")
            return False

        # Application configuration package.
        if appconfigDict.has_key('source_file') and delivDict.has_key('appconfig'):
            appconfig = delivDict['appconfig']
            appconfigTarName = os.path.basename(appconfig)
            appconfigDestFile = os.path.join(catalogBaseDir, appconfigTarName)

            if isDebug():
                print("DEBUG: Copying %s to %s" % (appconfig, appconfigDestFile))

            try:
                shutil.copy(appconfig, appconfigDestFile)
                os.chmod(appconfigDestFile, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
            except Exception as e:
                print(e)
                return False

        elif appconfigDict.has_key('import_url'):
            appconfigTarName = 'undefined'
        else:
            print("ERROR: 'appconfig autogen|file|url <args>' must be executed before packaging.")
            return False

        if appconfigDict.has_key('config_api_version'):
            configApiVersion = str(appconfigDict['config_api_version'])
        else:
            print("ERROR: appconfig's 'config_api_version' is undefined.")
            return False

        # Logo file
        if logoDict.has_key('source_file') and delivDict.has_key('logo'):
            logo = delivDict['logo']
            logoMD5 =  delivDict['logoSum']

            compressedLogoFile = os.path.join(catalogStagingDir, os.path.basename(logo) + ".gz")

            try:
                if isDebug():
                    print("DEBUG: Compressing %s to %s" % (logo, compressedLogoFile))

                with open(logo, 'rb') as logoFileDesc:
                    compressedFile = gzip.open(compressedLogoFile, 'wb')
                    compressedFile.writelines(logoFileDesc)
                    compressedFile.close()

                if isDebug():
                    print("DEBUG: Encoding %s into base64" % (compressedLogoFile))

                p = subprocess.Popen(["base64", "-w0", compressedLogoFile],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
                logoEncodedData, err = p.communicate()
                if err != '':
                    print("ERROR: Failed to encode the compressed logo file.")
                    return False
            except Exception as e:
                print("ERROR: Failed to compress and encode the logo file.", e)
                return False
        elif not logoDict.has_key('import_url'):
            print("WARN: No logo to include in the bundle.")
            logoEncodedData = "undefined"
            logoMD5 = "undefined"

        # Source files
        if delivDict.has_key('sources'):
            sources = delivDict['sources']
            sourceDestDirname = bundleName + "-src"
            sourcePackageName = sourceDestDirname + '.tgz'

            sourceDestDir = os.path.join(catalogStagingDir, sourceDestDirname)
            sourceTarDest = os.path.join(catalogBaseDir, sourcePackageName)

            if os.path.exists(sourceDestDir):
                shutil.rmtree(sourceDestDir)

            os.makedirs(sourceDestDir)
            copyCmd = "cp -rpf %s %s" % (' '.join(sources), sourceDestDir)
            tarCmd = "tar -C %s -czf %s %s" % (catalogStagingDir, sourceTarDest, sourceDestDirname)

            if isDebug():
                print("DEBUG: Creating source tarball %s" % (sourceTarDest))

            if executeShellCmd(copyCmd):
                if not executeShellCmd(tarCmd):
                    return False
            else:
                return False
        else:
            sourcePackageName = 'undefined'

        # Is distro dependent on someother distro?
        if entryDict.has_key('distro_dependency')  or \
            entryDict.has_key('service_dependencies'):
            independent = 'false'
        else:
            independent = 'true'

        # Image files
        imageFileNames = []
        for imageDict in imageDictList:
            img = imageDict.get('imageFile', None)
            if img != None:
                imgRoles = imageDict['imageRoles']
                if imgRoles == DEFAULT_IMAGE_ROLES:
                    imgRoles = []
                    for roleDict in entryDict.get("node_roles", []):
                        imgRoles.append(roleDict['id'])

                print("Copying %s for roles: %s." % (os.path.abspath(img),
                                                     ','.join(imgRoles)))

                shutil.copy(img, catalogBaseDir)

                imgFileName = os.path.basename(img)
                imageFileNames.append(imgFileName)

                # Remove some fields in the ImageDict as they are not
                # needed in the bundle feed.
                imageDict.pop("imageFile", None)
                imageDict.pop("imageChecksum", None)

        # Convert the list of image dictionaries to a string. However, we
        # are going to replace this text into a schell script (decompress.sh)
        # so we have to quote the double-quotes.
        imageDictStr = json.dumps(imageDictList).replace('"', '\\"')
        registryDictStr = json.dumps(registryDict). replace('"', '\\"')

        # Time to package all the components.
        #      1. Create the tar file of all the contents
        #      2. Populate decompress.sh
        #      3. create the bin file.
        bundleTarFile = catalogBaseDir + '.tar'
        bundleTarChecksum = ''

        bundleTarCmd = "tar -C %s -cf %s %s" % (os.path.dirname(catalogBaseDir),
                                                bundleTarFile,
                                                bundleName)
        if executeShellCmd(bundleTarCmd):
            # Calcluate the md5sum of the file
            bundleTarChecksum = calculateMD5SUM(bundleTarFile)
        else:
            return False

        # Populate the decompress.sh template
        try:
            with open(os.path.join(BUNDLE_BUILD_DIR, 'decompress_v4.sh')) as f:
                decompressData = f.read()
        except Exception as e:
            print("ERROR: Failed to read template for packaging.", e)
            return False

        decompressData = decompressData\
                            .replace('@@@@BUNDLENAME@@@@', bundleName)\
                            .replace('@@@NAME@@@', entryDict['label']['name'])\
                            .replace('@@@DESCRIPTION@@@', entryDict['label']['description'])\
                            .replace('@@@VERSION@@@', entryDict['version'])\
                            .replace('@@@DISTRO@@@', distroId)\
                            .replace('@@@@BUILDTYPE@@@@', 'release')\
                            .replace('@@@CONFIGAPIVER@@@', configApiVersion)\
                            .replace('@@@CATALOGAPIVER@@@', str(entryDict['catalog_api_version']))\
                            .replace('@@@BUILTONDOCKER@@@', delivDict['built_on_docker'])\
                            .replace('@@@INDEPENDENT@@@', independent)\
                            .replace('@@@@LOGOEXTRACTDIR@@@@', LOGO_EXTRACT_DIR)\
                            .replace('@@@@LOGO_ENC_DATA@@@@', logoEncodedData)\
                            .replace('@@@@LOGOCHECKSUM@@@@', logoMD5)\
                            .replace('@@@@TARENTRYJSON@@@@', entryFileName)\
                            .replace('@@@@TARENTRYSETUP@@@@', appconfigTarName)\
                            .replace('@@@SOURCEPACKAGE@@@', sourcePackageName)\
                            .replace('@@@IMAGEOSTYPES@@@', ','.join(imageOsTypes))\
                            .replace('@@@@TARENTRYIMAGES@@@@', ' '.join(imageFileNames))\
                            .replace('@@@IMAGESDICT@@@', imageDictStr)\
                            .replace('@@@REGISTRY@@@', registryDictStr)\
                            .replace('@@@@TAREXTRACTDIR@@@@', CATALOG_EXTRACT_DIR)\
                            .replace('@@@@TARFILECHECKSUM@@@@', bundleTarChecksum)

        if isDebug():
            # Save the decompress data to a file.
            decompDestFile = os.path.join(catalogStagingDir, 'decompress.sh')
            with open(decompDestFile, 'w') as decompFileObj:
                decompFileObj.write(decompressData)

        # Create the bundle file.
        if not os.path.exists(delivDir):
            os.makedirs(delivDir)

        catalogBundleFile = os.path.join(delivDir, bundleName + '.bin')
        with open(catalogBundleFile, 'wb') as bundleFileObj:
            bundleFileObj.write(decompressData)
            with open(bundleTarFile, 'rb') as bundleTarObj:
                for buf in iter(lambda: bundleTarObj.read(4096), b""):
                    bundleFileObj.write(buf)

        os.chmod(catalogBundleFile, stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)
        print("\nCatalog bundle saved at %s" % (catalogBundleFile))

        return True

    def complete(self, text, argsList):
        return []

    def _is_url(self, filed):
        return filed.startswith('http://') or filed.startswith('https://')


__all__ = ['CatalogPackageV5']
