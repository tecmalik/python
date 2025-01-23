
countries = {
    "usa": {"california": {"Los Angeles": 4_000_000, "san francisco": 8700_00}},
    "canada": {"Ontario": {"Toronto": 2_930_000, "Ottawa": 994_837}}
}
country = "Nigeria"
state = { "Lagos": {"mainland": 42_000_329, "ikorodu": 4_230_00}}

#update

def get_citys_and_population(new_country, states):
    for country, in countries.item():
        states[country] = state[country]

