import pickle
import streamlit as st
import pandas as pd

# Load the pre-trained model
KMeans = pickle.load(open('model.pkl', 'rb'))

# Define the prediction function
def predict(birth_rate, business_tax_rate, co2_emissions, days_to_start_business, gdp, health_exp_gdp,
            health_exp_per_capita, hours_to_do_tax, infant_mortality_rate, internet_usage, lending_interest,
            mobile_phone_usage, population_65_plus, population_total, population_urban, tourism_inbound, tourism_outbound):
    
    # Prepare input data for prediction
    input_data = pd.DataFrame([[birth_rate, business_tax_rate, co2_emissions, days_to_start_business, gdp,
                                health_exp_gdp, health_exp_per_capita, hours_to_do_tax, infant_mortality_rate,
                                internet_usage, lending_interest, mobile_phone_usage, population_65_plus,
                                population_total, population_urban, tourism_inbound, tourism_outbound]],
                               columns=['Birth Rate', 'Business Tax Rate', 'CO2 Emissions', 'Days to Start Business',
                                        'GDP', 'Health Exp % GDP', 'Health Exp/Capita', 'Hours to do Tax',
                                        'Infant Mortality Rate', 'Internet Usage', 'Lending Interest',
                                        'Mobile Phone Usage', 'Population 65+', 'Population Total',
                                        'Population Urban', 'Tourism Inbound', 'Tourism Outbound'])
    
    prediction = KMeans.predict(input_data)
    return prediction

# Main function to run the Streamlit app
def main():
    st.title("World Development Measurement Clustering Analysis")
    st.markdown('This is a simple webapp for prediction of cluster labels based on various economic indicators :chart:')

    # Collect user input for the features
    birth_rate = st.number_input('Birth Rate')
    business_tax_rate = st.number_input('Business Tax Rate')
    co2_emissions = st.number_input('CO2 Emissions')
    days_to_start_business = st.number_input('Days to Start Business')
    gdp = st.number_input('GDP')
    health_exp_gdp = st.number_input('Health Exp % GDP')
    health_exp_per_capita = st.number_input('Health Exp/Capita')
    hours_to_do_tax = st.number_input('Hours to do Tax')
    infant_mortality_rate = st.number_input('Infant Mortality Rate')
    internet_usage = st.number_input('Internet Usage')
    lending_interest = st.number_input('Lending Interest')
    mobile_phone_usage = st.number_input('Mobile Phone Usage')
    population_65_plus = st.number_input('Population 65+')
    population_total = st.number_input('Population Total')
    population_urban = st.number_input('Population Urban')
    tourism_inbound = st.number_input('Tourism Inbound')
    tourism_outbound = st.number_input('Tourism Outbound')

    if st.button('Predict'):
        # Make prediction
        result = predict(birth_rate, business_tax_rate, co2_emissions, days_to_start_business, gdp, health_exp_gdp,
                          health_exp_per_capita, hours_to_do_tax, infant_mortality_rate, internet_usage,
                          lending_interest, mobile_phone_usage, population_65_plus, population_total,
                          population_urban, tourism_inbound, tourism_outbound)
         
        # Display result
        st.success(f"The predicted cluster label for the given data is: {result[0]}")
 
if __name__ == '__main__':
    main()
