from Geoserver import Geoserver
from ColorMap import colorEntryMap
import os


service_url = 'http://geoserver:8080/geoserver'
username = 'admin'
password = 'geoserver'
geo = Geoserver(service_url=service_url, username=username, password=password)

def createData(source='TIFSource'):
    PATH = os.path.split(__file__)[0]
    pathTIFSource = os.path.join(PATH, source)
    geoParam = []
    workSpaceList = []
    for root, dirs, files in os.walk(pathTIFSource):
        for file in files:
            workspace = os.path.split(root)[-1]
            filename = file.split(".")[0]
            pathLayer = os.path.join(root, file)
            colorType = colorEntryMap[workspace]['type']
            if '-' in colorEntryMap[workspace]:
                colorEntry = colorEntryMap[workspace]['-']
            else:
                colorEntry = colorEntryMap[workspace][filename]
            geoParam.append({
                'workspace': workspace,
                'layerName': filename,
                'sldName': filename,
                'pathLayer': pathLayer,
                'colorEntry': colorEntry,
                'colorType': colorType
            })
            workSpaceList.append(workspace)
    return geoParam, set(workSpaceList)


# 创建资源
geoParam, workSpaceList = createData(source='TIFSource')
# 创建工作空间
for workspace in workSpaceList:
    geo.create_workspace(workspace=workspace)
# 创建图层，Style
for geoItem in geoParam:
    geo.create_coveragestore(layerName=geoItem['layerName'], workspace=geoItem['workspace'], pathLayer=geoItem['pathLayer'])
    geo.create_coveragestyle(sldName=geoItem['sldName'], workspace=geoItem['workspace'], colorEntry=geoItem['colorEntry'], colorType=geoItem['colorType'])
    geo.publish_style(layerName=geoItem['layerName'], sldName=geoItem['sldName'], workspace=geoItem['workspace'])
