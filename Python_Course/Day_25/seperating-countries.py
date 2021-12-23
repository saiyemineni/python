import pandas as pd

countries = {'AT':'Austria (European Union)','BE':'Belgium (European Union)','BG':'Bulgaria (European Union)','HR':'Croatia (European Union)','CA':'Canada','CY':'Cyprus (European Union)','CZ':'Czech Republic (European Union)','DK':'Denmark (European Union)','EE':'Estonia (European Union)','FI':'Finland (European Union)','FR':'France (European Union)','DE':'Federal Republic of Germany (European Union)','GR':'Greece (European Union)','HU':'Hungary (European Union)','IE':'Ireland (European Union)','IT':'Italy (European Union)','LV':'Latvia (European Union)','LT':'Lithuania (European Union)','LU':'Luxembourg (European Union)','MT':'Malta (European Union)','NL':'The Netherlands (European Union)','PL':'Poland (European Union)','PT':'Portugal (European Union)','RO':'Romania (European Union)','SK':'Slovakia (European Union)','SI':'Slovenia (European Union)','ES':'Spain (European Union)','SE':'Sweden (European Union)','GB':'United Kingdom (European Union)','NZ':'New Zealand (European Union)','CG':'Republic of Congo (European Union)'};


for country in countries:
    country_name = countries[country].split("(")[0]
    country_trim = country_name.strip()
    print(country_name)
    with open('countries.txt', mode='a') as file:
        file.write(country_name+"\n")
