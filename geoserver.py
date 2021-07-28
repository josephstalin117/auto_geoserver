import pycurl
import os


class DataProvider(object):
    def __init__(self, data):
        self.data = data
        self.finished = False

    def read_cb(self, size):
        assert len(self.data) <= size
        if not self.finished:
            self.finished = True
            return self.data
        else:
            return ""


class FileReader:
    def __init__(self, fp):
        self.fp = fp

    def read_callback(self, size):
        return self.fp.read(size)


class Geoserver:
    def __init__(self, service_url='http://localhost:8080/geoserver', username='admin', password='geoserver'):
        self.service_url = service_url
        self.username = username
        self.password = password

    def create_workspace(self, workspace):
        try:
            c = pycurl.Curl()
            workspace_xml = "<workspace><name>{0}</name></workspace>".format(workspace)
            c.setopt(pycurl.USERPWD, self.username + ':' + self.password)
            c.setopt(c.URL, '{0}/rest/workspaces'.format(self.service_url))
            c.setopt(pycurl.HTTPHEADER, ["Content-type: text/xml"])
            c.setopt(pycurl.POSTFIELDSIZE, len(workspace_xml))
            c.setopt(pycurl.READFUNCTION, DataProvider(workspace_xml).read_cb)
            c.setopt(pycurl.POST, 1)
            c.perform()
            c.close()
        except Exception as e:
            return 'Error: {}'.format(e)


    def create_coveragestore(self, pathLayer, workspace, layerName, file_type='GeoTIFF', content_type='image/tiff', overwrite=False):
        try:
            c = pycurl.Curl()
            c.setopt(pycurl.USERPWD, self.username + ':' + self.password)
            file_type = file_type.lower()
            c.setopt(c.URL, '{0}/rest/workspaces/{1}/coveragestores/{2}/file.{3}'.format(self.service_url, workspace, layerName, file_type))
            c.setopt(pycurl.HTTPHEADER, ["Content-type:{}".format(content_type)])
            c.setopt(pycurl.READFUNCTION, FileReader(open(pathLayer, 'rb')).read_callback)
            c.setopt(pycurl.INFILESIZE, os.path.getsize(pathLayer))
            if overwrite:
                c.setopt(pycurl.PUT, 1)
            else:
                c.setopt(pycurl.POST, 1)
            c.setopt(pycurl.UPLOAD, 1)
            c.perform()
            c.close()
        except Exception as e:
            return 'Error: {}'.format(e)


    def create_coveragestyle(self, workspace, colorEntry, sldName, colorType, overwrite=False):
        try:
            self.coverage_style_xml(colorEntry, sldName, colorType)
            style_xml = "<style><name>{0}</name><filename>{1}</filename></style>".format(sldName, sldName+'.sld')

            c = pycurl.Curl()
            c.setopt(pycurl.USERPWD, self.username + ':' + self.password)
            c.setopt(c.URL, '{0}/rest/workspaces/{1}/styles'.format(self.service_url, workspace))
            c.setopt(pycurl.HTTPHEADER, ['Content-type:text/xml'])
            c.setopt(pycurl.POSTFIELDSIZE, len(style_xml))
            c.setopt(pycurl.READFUNCTION, DataProvider(style_xml).read_cb)
            if overwrite:
                c.setopt(pycurl.PUT, 1)
            else:
                c.setopt(pycurl.POST, 1)
            c.perform()

            c.setopt(c.URL, '{0}/rest/workspaces/{1}/styles/{2}'.format(self.service_url, workspace, sldName))
            c.setopt(pycurl.HTTPHEADER, ["Content-type:application/vnd.ogc.sld+xml"])
            c.setopt(pycurl.READFUNCTION, FileReader(open('style.sld', 'rb')).read_callback)
            c.setopt(pycurl.INFILESIZE, os.path.getsize('style.sld'))
            if overwrite:
                c.setopt(pycurl.PUT, 1)
            else:
                c.setopt(pycurl.POST, 1)
            c.setopt(pycurl.UPLOAD, 1)
            c.perform()
            c.close()

            os.remove('style.sld')
        except Exception as e:
            return 'Error: {}'.format(e)


    def publish_style(self, layerName, sldName, workspace, content_type='text/xml'):
        try:
            c = pycurl.Curl()
            style_xml = "<layer><defaultStyle><name>{0}</name></defaultStyle></layer>".format(sldName)
            c.setopt(pycurl.USERPWD, self.username + ':' + self.password)
            c.setopt(c.URL, '{0}/rest/layers/{1}:{2}'.format(self.service_url, workspace, layerName))
            c.setopt(pycurl.HTTPHEADER, ["Content-type: {}".format(content_type)])
            c.setopt(pycurl.POSTFIELDSIZE, len(style_xml))
            c.setopt(pycurl.READFUNCTION, DataProvider(style_xml).read_cb)
            c.setopt(pycurl.PUT, 1)
            c.perform()
            c.close()
        except Exception as e:
            return 'Error: {}'.format(e)

    def coverage_style_xml(self, colorEntry, sldName, colorType):
        """
        colorType: ramp 渐变 intervals 分类
        """
        styleAppend = ''
        for item in colorEntry:
            styleAppend += '<sld:ColorMapEntry color="{}" label="{}" quantity="{}" opacity="{}"/>'.format(
                item['color'], item['label'], item['quantity'], item['opacity'])

        style = """
        <StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:gml="http://www.opengis.net/gml" version="1.0.0" xmlns:ogc="http://www.opengis.net/ogc" xmlns:sld="http://www.opengis.net/sld">
        <UserLayer>
            <sld:LayerFeatureConstraints>
            <sld:FeatureTypeConstraint/>
            </sld:LayerFeatureConstraints>
            <sld:UserStyle>
            <sld:Name>{2}</sld:Name>
            <sld:FeatureTypeStyle>
                <sld:Rule>
                <sld:RasterSymbolizer>
                    <sld:ChannelSelection>
                    <sld:GrayChannel>
                        <sld:SourceChannelName>1</sld:SourceChannelName>
                    </sld:GrayChannel>
                    </sld:ChannelSelection>
                    <sld:ColorMap type="{0}">
                        {1}
                    </sld:ColorMap>
                </sld:RasterSymbolizer>
                </sld:Rule>
            </sld:FeatureTypeStyle>
            </sld:UserStyle>
        </UserLayer>
        </StyledLayerDescriptor>
        """.format(colorType, styleAppend, sldName)

        with open('style.sld', 'w') as f:
            f.write(style)