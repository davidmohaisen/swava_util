import pickle
def insert_pair(vendor_prodIncons, ven, prod1, prod2):
    found = 0
    if ven in vendor_prodIncons:
        productDict = vendor_prodIncons[ven]
        for prod in productDict:
            if prod1 in productDict[prod]:
                productDict[prod].add(prod2)
                found = 1
            elif prod2 in productDict[prod]:
                productDict[prod].add(prod1)
                found = 1
        if found == 0:
            productDict[prod1] = set()
            productDict[prod1].add(prod2)
            productDict[prod1].add(prod1)
    else:
        vendor_prodIncons[ven] = {}
        vendor_prodIncons[ven][prod1] = set()
        vendor_prodIncons[ven][prod1].add(prod2)
        vendor_prodIncons[ven][prod1].add(prod1)
    return vendor_prodIncons

f2 = open('../../../../ConsistentVendor_prod_info-V2.csv', 'rb')
vendor_productCveCounts, vendor_productCves = {}, {}
Wotkn_TknVendorMap = {}
for line in f2:
    line = line.decode().replace('\n', '').rsplit(';')
    cve = line[0]
    vend = line[1]
    if vend == "":
        vend = line[2]
    # print(line)
    product = line[3]
    date = line[4]
    venP = vend+":"+product
    venWo = vend.replace('_', '').replace('-', '')

    if vend not in vendor_productCves:
        vendor_productCves[vend]  = {}
        if product not in vendor_productCves[vend]:
            vendor_productCves[vend][product] = set()
            vendor_productCves[vend][product].add(cve)
        else:
            vendor_productCves[vend][product].add(cve)
    else:
        if product not in vendor_productCves[vend]:
            vendor_productCves[vend][product] = set()
            vendor_productCves[vend][product].add(cve)
        else:
            vendor_productCves[vend][product].add(cve)

    if venWo not in vendor_productCves:
        vendor_productCves[venWo] = {}
        if product not in vendor_productCves[venWo]:
            vendor_productCves[venWo][product] = set()
            vendor_productCves[venWo][product].add(cve)
        else:
            vendor_productCves[venWo][product].add(cve)
    else:
        if product not in vendor_productCves[venWo]:
            vendor_productCves[venWo][product] = set()
            vendor_productCves[venWo][product].add(cve)
        else:
            vendor_productCves[venWo][product].add(cve)

# print(vendor_productCves['microsoft'])
# for itm in vendor_productCves:
#     if len(vendor_productCves[itm]) > 2:
#         print(itm, vendor_productCves[itm])
# exit()
    # print(line)
    # exit()
x = {'mozilla': {'nss': ['network_security_services']}, 'sun': {'jre': ['java_runtime_environment']}, 'cisco': {'ucs': ['unified_computing_system'], 'asa': ['adaptive_security_appliance'], 'crs': ['carrier_routing_system', 'customer_response_solution']}, 'intel': {'ipmi': ['intelligent_platform_management_interface']}, 'audiocoding': {'faad2': ['freeware_advanced_audio_decoder_2']}, 'sap': {'basis': ['business_application_software_integrated_solution'], 'ui': ['ui_infra']}, 'mcafee': {'cma': ['common_management_agent']}, 'otrs': {'otrs': ['open_ticket_request_system']}, 'asustor': {'adm': ['asustor_data_master']}, 'paypal': {'ipn': ['instant_payment_notification']}, 'silc': {'silc': ['secure_internet_live_conferencing']}, 'iomega': {'nas': ['network_attached_storage']}, 'terramaster': {'tos': ['terramaster_operating_system']}, 'mattblaze': {'cfs': ['cryptographic_file_system']}, 'massiveentertainment': {'wic': ['world_in_conflict']}, 'displaysuiteproject': {'ds': ['display_suite']}, 'ana': {'ana': ['all_nippon_airways']}, 'myupb': {'upb': ['ultimate_php_board']}, 'rsbac': {'rsbac': ['rule_set_based_access_control']}, 'lbstone': {'apb': ['active_php_bookmarks']}, 'windows': {'ie': ['internet_explorer'], 'adam': ['active_directory_application_mode'], 'iis': ['internet_information_server', 'internet_information_services']}, 'google': {'wt': ['web_toolkit']}, 'x': {'xdm': ['x_display_manager']}, 'chetcpasswd': {'sarg': ['squid_analysis_report_generator']}, 'wink': {'vcl': ['virtual_computing_lab']}, 'lms': {'lms': ['lan_management_system']}, 'alienvault': {'ossim': ['open_source_security_information_management']}, 'bestpractical': {'rt': ['request_tracker']}, 'gnome': {'gdm': ['gnome_display_manager'], 'eog': ['eye_of_gnome']}, 'npm': {'npm': ['node_packaged_modules']}, 'ubuntu': {'maas': ['metal_as_a_service']}, 'aiocp': {'aiocp': ['all_in_one_control_panel']}, 'horde': {'imp': ['internet_mail_program'], 'apt': ['advanced_package_tool']}, 'offl': {'offl': ['online_fantasy_football_league']}, 'misp': {'misp': ['malware_information_sharing_platform']}, 'simplemachines': {'smf': ['simple_machines_forum']}, 'mispproject': {'misp': ['malware_information_sharing_platform']}, 'helpcenterlive': {'hcl': ['help_center_live']}}
vendorset = set()
vendor_prodIncons = {}
for ven in x:
    productset = x[ven]
    vendorset.add(ven)

    y2 = {}
    for prod in productset:
        y = set(productset[prod])
        y.add(prod)
        y2[prod]=y
        # print(ven, prod, set(productset[prod]), y)#.add(prod))
    vendor_prodIncons[ven] = y2

    #     exit()
    # print(itm, x[itm], itm2, set(x[itm][itm2]))
# print("******")
# print(vendor_prodIncons['horde'])
# exit()
f = open('./editDistanceVendorProd1Prod2.csv', 'rb')
for line in f:
    line = line.decode().replace('\n', '').rsplit(":")
    vendor = line[0]
    editdist = int(line[1])
    prod1 = line[2]
    prod2 = line[3]
    if editdist != 0:
        continue
    vendorset.add(vendor)
    vendor_prodIncons = insert_pair(vendor_prodIncons, vendor, prod1, prod2)
    # print(len(vendor_prodIncons))
    # print(line)
# exit()
vendPairs = {'adobe:1:lifecycle:livecycle', 'adobe:1:lifecycle_data_services:livecycle_data_services', 'alexphpteam:1:alex_guestbook:@lex_guestbook', 'atmail:1:atmail:@tmail', 'bitcoin:1:bitcoin-qt:qitcoin-qt', 'mozilla:1:geckb:gecko', 'nativesolutions:1:tbe_banner_engine:the_banner_engine', 'rockwellautomation:1:softlogix:softlogic', 'soumu:1:soumu_workflow:soumo_workflow', 'sweetphp:1:totalcalender:totalcalendar'}
for line in vendPairs:
    line = line.rsplit(":")
    vendor = line[0]
    editdist = int(line[1])
    prod1 = line[2]
    prod2 = line[3]
    vendorset.add(vendor)
    vendor_prodIncons = insert_pair(vendor_prodIncons, vendor, prod1, prod2)
    # print(len(vendor_prodIncons))


x= 0
vendor_prod_maxProd = {}
for ven in vendor_prodIncons:
    # if ven != "mozilla":
    #     continue
    prodDict = vendor_prodIncons[ven]
    # print(ven, prodDict)
    # exit()
    if ven == 'prosetun':
        continue
    prodSetForMap = vendor_productCves[ven]
    # print(prodSetForMap)
    # exit()

    prod_maxProd = {}
    for prods in prodDict:
        x+=len(prodDict[prods])
        maxProd = ""
        maxCnt = 0
        for indivProd in prodDict[prods]:
            try:
                vulnCount = len(prodSetForMap[indivProd])
                # print()
            except:
                # print(ven, prodDict, indivProd)
                continue

            if vulnCount > maxCnt:
                maxCnt = vulnCount
                maxProd = indivProd
                # print(ven, indivProd, maxProd)
        if maxProd != "":
            for indivProd in prodDict[prods]:
                prod_maxProd[indivProd] = maxProd
                # print(ven, indivProd, maxProd)

    vendor_prod_maxProd[ven] = prod_maxProd


        # out = str(ven) + ";" + str(prod) + ";" + str(len(prodDict[prod]))
        # with open('./PureInconsCounts.csv', 'a') as foo:
        #     foo.write(out + '\n')
print(vendor_prod_maxProd)
fout = open('./vendor_prod_maxProd.pkl', 'wb')
pickle.dump(vendor_prod_maxProd, fout)


print("Total Inconsistent Products: ", x)
# fout = open('./vendor_prodIncons.pkl', 'wb')
# pickle.dump(vendor_prodIncons, fout)

print(vendorset)
print(len(vendorset))
print(vendor_prodIncons.keys())
print(len(vendor_prodIncons.keys()))
impactedVendors = set(vendor_prodIncons.keys())
# fout = open('./impactedVendorsByProdIncons.pkl', 'wb')
# pickle.dump(impactedVendors, fout)