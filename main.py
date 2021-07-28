from Geoserver import Geoserver
#from ColorMap import colorEntryMap
import os

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

def createData2(colorEntryMap, source, workspace):
    PATH = os.path.split(__file__)[0]
    pathTIFSource = os.path.join(PATH, source)
    geoParam = []
    workSpaceList = []
    for root, dirs, files in os.walk(pathTIFSource):
        for file in files:
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



if __name__ == '__main__':
    service_url = 'http://172.18.10.204:6079/geoserver'
    username = 'admin'
    password = 'geoserver'
    geo = Geoserver(service_url=service_url, username=username, password=password)

    colorEntryMap = {
    'blackodor': {
        'type': 'ramp',
        '-': [
                {'color': '#000000', 'quantity': '0', 'label': '', 'opacity': '0'},
                {'color': '#FF0000', 'quantity': '1', 'label': 'blackodor', 'opacity': '1'},
                {'color': '#0000FF', 'quantity': '2', 'label': 'nwater', 'opacity': '1'}
            ]
        }
    }

    # 创建资源
    geoParams, workSpaceList = createData2(colorEntryMap, source='tif_source/black_odor', workspace='blackodor')
    # 创建图层，Style
    for geoItem in geoParams:
        geo.create_coveragestore(layerName=geoItem['layerName'], workspace=geoItem['workspace'], pathLayer=geoItem['pathLayer'])
        geo.create_coveragestyle(sldName=geoItem['sldName'], workspace=geoItem['workspace'], colorEntry=geoItem['colorEntry'], colorType=geoItem['colorType'])
        geo.publish_style(layerName=geoItem['layerName'], sldName=geoItem['sldName'], workspace=geoItem['workspace'])

    # 创建工作空间
    #for workspace in workSpaceList:
    #    geo.create_workspace(workspace=workspace)
