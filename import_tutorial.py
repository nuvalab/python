def filter_countries(countries, country_filter):
    filtered_countries = []
    
    for i in countries:
        if i.startswith(country_filter):
            filtered_countries.append(i)
    
    return filtered_countries

def get_first_country(countries):
    return countries[0]


# countries = ["Spain", "Sweeden", "Germany", "Colombia", "Scotland", "Canada"]

# print(filter_countries(countries, "C"))