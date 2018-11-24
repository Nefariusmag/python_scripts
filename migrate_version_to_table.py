import json
import requests
import os

user = os.getenv('USER_CONFLUENCE', 'test-user')
password = os.getenv('PASSSWORD_CONFLUENCE', '')
conf_url = 'http://conf.ru/rest/api/content/'
page = os.getenv('PAGE_CONFLUENCE', '26575536')
file = '/tmp/VERSIONS'
# os.chdir('parse-versions-table')


# генерация словаря на основе файла VERSIONS
def generate_list(file_with_version):
    global clean_five
    file_versions = open(file_with_version, 'r')
    text = file_versions.read().strip()
    file_versions.close()
    clean_one = text.split('\n\n')
    clean_five = {}
    for i in range(len(clean_one)):
        clean_two = clean_one[i].split(':')
        for n in range(len(clean_two)):
            if '.ru' not in clean_two[n]:
                clean_three = clean_two[n].split('\n')
                for s in range(len(clean_three)):
                    clean_four = clean_three[s].split(' - ')
                    if len(clean_three) == 2:
                        if len(clean_four) == 2:
                            clean_five[clean_two[0]] = {clean_three[1].split(' - ')[0]: clean_three[1].split(' - ')[1]}
                    if len(clean_three) == 3:
                        if len(clean_four) == 2:
                            clean_five[clean_two[0]] = {clean_three[1].split(' - ')[0]: clean_three[1].split(' - ')[1],
                                                        clean_three[2].split(' - ')[0]: clean_three[2].split(' - ')[1]}
                    if len(clean_three) == 4:
                        if len(clean_four) == 2:
                            clean_five[clean_two[0]] = {clean_three[1].split(' - ')[0]: clean_three[1].split(' - ')[1],
                                                        clean_three[2].split(' - ')[0]: clean_three[2].split(' - ')[1],
                                                        clean_three[3].split(' - ')[0]: clean_three[3].split(' - ')[1]}
                    if len(clean_three) == 5:
                        if len(clean_four) == 2:
                            clean_five[clean_two[0]] = {clean_three[1].split(' - ')[0]: clean_three[1].split(' - ')[1],
                                                        clean_three[2].split(' - ')[0]: clean_three[2].split(' - ')[1],
                                                        clean_three[3].split(' - ')[0]: clean_three[3].split(' - ')[1],
                                                        clean_three[4].split(' - ')[0]: clean_three[4].split(' - ')[1]}
                    if len(clean_three) == 6:
                        if len(clean_four) == 2:
                            clean_five[clean_two[0]] = {clean_three[1].split(' - ')[0]: clean_three[1].split(' - ')[1],
                                                        clean_three[2].split(' - ')[0]: clean_three[2].split(' - ')[1],
                                                        clean_three[3].split(' - ')[0]: clean_three[3].split(' - ')[1],
                                                        clean_three[4].split(' - ')[0]: clean_three[4].split(' - ')[1],
                                                        clean_three[5].split(' - ')[0]: clean_three[5].split(' - ')[1]}
                    if len(clean_three) == 7:
                        if len(clean_four) == 2:
                            clean_five[clean_two[0]] = {clean_three[1].split(' - ')[0]: clean_three[1].split(' - ')[1],
                                                        clean_three[2].split(' - ')[0]: clean_three[2].split(' - ')[1],
                                                        clean_three[3].split(' - ')[0]: clean_three[3].split(' - ')[1],
                                                        clean_three[4].split(' - ')[0]: clean_three[4].split(' - ')[1],
                                                        clean_three[5].split(' - ')[0]: clean_three[5].split(' - ')[1],
                                                        clean_three[6].split(' - ')[0]: clean_three[6].split(' - ')[1]}
                    if len(clean_three) == 12:
                        if len(clean_four) == 2:
                            clean_five[clean_two[0]] = {clean_three[1].split(' - ')[0]: clean_three[1].split(' - ')[1],
                                                        clean_three[2].split(' - ')[0]: clean_three[2].split(' - ')[1],
                                                        clean_three[3].split(' - ')[0]: clean_three[3].split(' - ')[1],
                                                        clean_three[4].split(' - ')[0]: clean_three[4].split(' - ')[1],
                                                        clean_three[5].split(' - ')[0]: clean_three[5].split(' - ')[1],
                                                        clean_three[6].split(' - ')[0]: clean_three[6].split(' - ')[1],
                                                        clean_three[7].split(' - ')[0]: clean_three[7].split(' - ')[1],
                                                        clean_three[8].split(' - ')[0]: clean_three[8].split(' - ')[1],
                                                        clean_three[9].split(' - ')[0]: clean_three[9].split(' - ')[1],
                                                        clean_three[10].split(' - ')[0]: clean_three[10].split(' - ')[1],
                                                        clean_three[11].split(' - ')[0]: clean_three[11].split(' - ')[1]}
                    if len(clean_three) == 15:
                        if len(clean_four) == 2:
                            clean_five[clean_two[0]] = {clean_three[1].split(' - ')[0]: clean_three[1].split(' - ')[1],
                                                        clean_three[2].split(' - ')[0]: clean_three[2].split(' - ')[1],
                                                        clean_three[3].split(' - ')[0]: clean_three[3].split(' - ')[1],
                                                        clean_three[4].split(' - ')[0]: clean_three[4].split(' - ')[1],
                                                        clean_three[5].split(' - ')[0]: clean_three[5].split(' - ')[1],
                                                        clean_three[6].split(' - ')[0]: clean_three[6].split(' - ')[1],
                                                        clean_three[7].split(' - ')[0]: clean_three[7].split(' - ')[1],
                                                        clean_three[8].split(' - ')[0]: clean_three[8].split(' - ')[1],
                                                        clean_three[9].split(' - ')[0]: clean_three[9].split(' - ')[1],
                                                        clean_three[10].split(' - ')[0]: clean_three[10].split(' - ')[1],
                                                        clean_three[11].split(' - ')[0]: clean_three[11].split(' - ')[1],
                                                        clean_three[13].split(' - ')[0]: clean_three[12].split(' - ')[1],
                                                        clean_three[13].split(' - ')[0]: clean_three[13].split(' - ')[1],
                                                        clean_three[14].split(' - ')[0]: clean_three[14].split(' - ')[1]}
                    if len(clean_three) == 22:
                        if len(clean_four) == 2:
                            clean_five[clean_two[0]] = {clean_three[1].split(' - ')[0]: clean_three[1].split(' - ')[1],
                                                        clean_three[2].split(' - ')[0]: clean_three[2].split(' - ')[1],
                                                        clean_three[3].split(' - ')[0]: clean_three[3].split(' - ')[1],
                                                        clean_three[4].split(' - ')[0]: clean_three[4].split(' - ')[1],
                                                        clean_three[5].split(' - ')[0]: clean_three[5].split(' - ')[1],
                                                        clean_three[6].split(' - ')[0]: clean_three[6].split(' - ')[1],
                                                        clean_three[7].split(' - ')[0]: clean_three[7].split(' - ')[1],
                                                        clean_three[8].split(' - ')[0]: clean_three[8].split(' - ')[1],
                                                        clean_three[9].split(' - ')[0]: clean_three[9].split(' - ')[1],
                                                        clean_three[10].split(' - ')[0]: clean_three[10].split(' - ')[1],
                                                        clean_three[11].split(' - ')[0]: clean_three[11].split(' - ')[1],
                                                        clean_three[12].split(' - ')[0]: clean_three[12].split(' - ')[1],
                                                        clean_three[13].split(' - ')[0]: clean_three[13].split(' - ')[1],
                                                        clean_three[14].split(' - ')[0]: clean_three[14].split(' - ')[1],
                                                        clean_three[15].split(' - ')[0]: clean_three[15].split(' - ')[1],
                                                        clean_three[16].split(' - ')[0]: clean_three[16].split(' - ')[1],
                                                        clean_three[17].split(' - ')[0]: clean_three[17].split(' - ')[1],
                                                        clean_three[18].split(' - ')[0]: clean_three[18].split(' - ')[1],
                                                        clean_three[19].split(' - ')[0]: clean_three[19].split(' - ')[1],
                                                        clean_three[20].split(' - ')[0]: clean_three[20].split(' - ')[1],
                                                        clean_three[21].split(' - ')[0]: clean_three[21].split(' - ')[1]}


# выкачать страницу
def get_page_json(page_id, expand=False):
    if expand:
        suffix = f"?expand={expand}"
    else:
        suffix = ""
    url = conf_url + page_id + suffix
    response = requests.get(url, auth=(user, password))
    response.encoding = "utf8"
    return json.loads(response.text)


# записать текущую таблицу в table.html
def write_conf_in_table_file():
    conf_json = get_page_json(page, "body.storage")
    fout = open('table.html', 'w')
    print(conf_json['body']['storage']['value'], file=fout)
    fout.close()


def get_stand(name_host):
    global stand
    if '-postzero-node1-i.dkp.lanit.ru' in name_host:
        stand = 'POSTZERO'
    elif '-node1-i.dkp.lanit.ru' in name_host:
        stand = 'DKP'
    elif '-test-node1-i.gis-tek.ru' in name_host:
        stand = 'REA_TEST'
    elif '-node1-i.gis-tek.ru' in name_host:
        stand = 'PI'
    elif '-pk-i.gistek.lanit.ru' in name_host:
        stand = 'PK'
    elif '10.200.200' in name_host:
        stand = 'ZERO'
    elif '10.100.190' in name_host:
        stand = 'REA_ZERO'


def get_url_repo(application):
    global git_url
    git_repo = ''
    if application == 'portal-iframe-int':
        git_repo = 'PORTAL/portal-iframe'
    # elif application == 'support-mail-int':
    #     git_repo = 'PORTAL/support-mail-portlet'
    elif application == 'inspinia-theme-int':
        git_repo = 'PORTAL/inspinia-theme'
    elif application == 'reports-display-int':
        git_repo = 'PORTAL/reports-display-portlet'
    elif application == 'iframe-hook-int':
        git_repo = 'PORTAL/portal-iframe'
    elif application == 'notification-int':
        git_repo = 'PORTAL/notification-portlet'
    elif application == 'smevinfo-int':
        git_repo = 'PORTAL/smev-info-portlet'
    elif application == 'npa-loader-hook-pub':
        git_repo = 'PORTAL/npa-loader-portlet'
    elif application == 'support-mail-pub':
        git_repo = 'PORTAL/support-mail-portlet'
    elif application == 'hook-search-pub' or application == 'hook-search-int':
        git_repo = 'PORTAL/hook-search'
    # elif application == '':
    #     git_repo = 'PORTAL/new-theme'
    elif application == 'asset-publisher-hook-pub':
        git_repo = 'PORTAL/hook-asset-publisher'
    elif application == 'languagePackRU-pub' or application == 'languagePackRU-int':
        git_repo = 'PORTAL/hook-languagePackRU'
    # elif application == '':
    #     git_repo = 'PORTAL/portal-parent'
    elif application == 'urc-theme-pub':
        git_repo = 'PORTAL/urc-theme'
    elif application == 'mainpageGEO-pub':
        git_repo = 'PORTAL/mainpageGeo'
    elif application == 'slider-pub':
        git_repo = 'PORTAL/slider'
    elif application == 'subsystem-search-pub' or application == 'subsystem-search-int':
        git_repo = 'PORTAL/subsystem-search'
    # elif application == '':
    #     git_repo = 'PORTAL/integrationFNS'
    elif application == 'integrationGASU-int':
        git_repo = 'PORTAL/integrationGASU'
    elif application == 'login-hook-int':
        git_repo = 'PORTAL/login-hook'
    # elif application == '':
    #     git_repo = 'PORTAL/integrationFTS'
    elif application == 'robot':
        git_repo = 'INFOSTREAM/robot'
    elif application == 'gtafo':
        git_repo = 'gistek-web/afo'
    elif application == 'registration':
        git_repo = 'gistek-web/registration'
    elif application == 'gtarm' or application == 'gttechnologist':
        git_repo = 'gistek-web/monitor'
    elif application == 'gtonl':
        git_repo = 'gistek-web/formfillonline'
    elif application == 'gtimpxml':
        git_repo = 'gistek-web/import-xml'
    elif application == 'gtxml':
        git_repo = 'gistek-web/create-xml'
    elif application == 'gttransport':
        git_repo = 'gistek-web/transport'
    elif application == 'gtcontrol':
        git_repo = 'gistek-web/control'
    elif application == 'gtexpgisee':
        git_repo = 'gistek-web/import-ps-ues-gisee'
    elif application == 'gtdownload':
        git_repo = 'gistek-web/download-arm'
    elif application == 'sso-server':
        git_repo = 'gistek-web/sso-server'
    elif application == 'gtclassifier':
        git_repo = 'gistek-web/classifier'
    elif application == 'classifier-view':
        git_repo = 'gistek-web/classifier-view'
    elif application == 'ticket':
        git_repo = 'gistek-web/ticket'
    elif application == 'loadssb':
        git_repo = 'gistek-web/loadssb'
    elif application == 'composer':
        git_repo = 'gistek-web/vendor'
    elif application == 'tek-forms-int':
        git_repo = 'MOBILE-APP/tek-portlet'
    elif application == 'mobile':
        git_repo = 'MOBILE-APP/web-service-java'
    elif application == 'POIB':
        git_repo = 'SECURITY/poib'
    elif application == 'mis' or application == 'transform' or application == 'export':
        git_repo = 'INTEGRATIONAL/is'
    elif application == 'generator':
        git_repo = 'INTEGRATIONAL/generator'
    elif application == 'logui':
        git_repo = 'INTEGRATIONAL/log-ui'
    elif application == 'gtprocessor':
        git_repo = 'INTEGRATIONAL/gtprocessor'
    elif application == 'fileProperties':
        git_repo = 'PENTAHO/pentaho-fileProperties'
    elif application == 'cas_tek':
        git_repo = 'PENTAHO/pentaho-cas-tek'
    elif application == 'quixote-theme':
        git_repo = 'PENTAHO/quixote-theme'
    elif application == 'LanguagePacks':
        git_repo = 'PENTAHO/pentahoLanguagePacks'
    elif application == 'pentaho_plugins':
        git_repo = 'PENTAHO/pentaho-plugins'
    git_url = f'http://git.gistek.lanit.ru/{git_repo}/blob/release/CHANGELOG.md#'


def use_node_script():
    global final_json
    for first_i in clean_five:
        for second_i in clean_five[first_i]:
            get_stand(first_i)
            component = second_i
            version = clean_five[first_i][second_i]
            get_url_repo(component)
            # print('node parse.js --html=table.html --target=' + stand + ' --component=' + component
                      # + ' --new-version=' + version + ' --new-version-link=' + git_url + version)
            app_without_version = {'PostgreSQL', 'Java', 'Tomcat', "Liferay", 'PHP', 'Apache', 'Pentaho', 'SpatialDB',
                                   'GISWebServiceSE', 'GISAdministratorSE', 'WSO', 'ActiveMQ'}
            if [x for x in app_without_version if x in second_i] == True:
                os.system(f'node parse.js --html=table.html --target={stand} --component={component}'
                          f' --new-version={version} --new-version-link={git_url}{version} --no-version=true')
            else:
                os.system(f'node parse.js --html=table.html --target={stand} --component={component}'
                          f' --new-version={version} --new-version-link={git_url}{version}')
    file_table = open('table.html', 'r')
    final_json = file_table.read().strip()
    file_table.close()


# переменные для новой версии страницы
def generate_new_version_page():
    global  new_json_data
    json_data = get_page_json(page)
    new_json_data = dict()
    new_json_data['id'] = json_data['id']
    new_json_data['type'] = json_data['type']
    new_json_data['title'] = json_data['title']
    new_json_data['type'] = json_data['type']
    new_json_data['version'] = {"number": json_data['version']['number'] + 1}
    if 'key' not in json_data:
        new_json_data['key'] = json_data['space']['key']
    else:
        new_json_data['key'] = json_data['key']
    new_json_data['body'] = {'storage': {'value': final_json, 'representation': 'storage'}}


# функция чтобы загрузить новую страницу в конфлюенс
def load_page_to_conf(page_id, json_content):
    headers = {
        'Content-Type': 'application/json',
    }
    json_content['body']['storage']['value'] = json_content['body']['storage']['value'].replace('"', '\'')
    response = requests.put(conf_url + page_id, headers=headers, data=json.dumps(json_content), auth=(user, password))
    return response


generate_list(file)
write_conf_in_table_file()
# показать что есть на текущей страничке
# print("То что есть")
# conf_json = get_page_json(page, "body.storage")
# print(conf_json['body']['storage']['value'])
use_node_script()
generate_new_version_page()
load_page_to_conf(page, new_json_data)
