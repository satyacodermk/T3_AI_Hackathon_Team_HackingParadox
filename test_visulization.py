import streamlit as st

data = {
    'year1': {
        'investment_recommendation': ['Real Estate', 'Stocks', 'Bonds'],
        'roadmap_to_achieve_goal': {
            'step1': {'action': 'Start emergency fund', 'risk_percentage': 10, 'success_percentage': 90},
            'step2': {'action': 'Invest in Real Estate', 'risk_percentage': 20, 'success_percentage': 80},
            'step3': {'action': 'Diversify with Stocks and Bonds', 'risk_percentage': 15, 'success_percentage': 85},
            'step4': {'action': 'Regularly review portfolio', 'risk_percentage': 10, 'success_percentage': 90},
        },
        'savings_plan_health_issues': 'Allocate funds for health expenses',
        'summary': 'Build emergency fund, invest in Real Estate, diversify, and allocate funds for health expenses.',
    },
    'year2': {
        'investment_recommendation': ['Stocks', 'Real Estate', 'Bonds'],
        'roadmap_to_achieve_goal': {
            'step1': {'action': 'Review and adjust portfolio', 'risk_percentage': 15, 'success_percentage': 85},
            'step2': {'action': 'Increase contributions', 'risk_percentage': 10, 'success_percentage': 90},
            'step3': {'action': 'Explore additional opportunities', 'risk_percentage': 20, 'success_percentage': 80},
            'step4': {'action': 'Reassess health-related expenses', 'risk_percentage': 15, 'success_percentage': 85},
        },
        'savings_plan_health_issues': 'Continue allocating funds for health expenses and review health insurance coverage.',
        'summary': 'Review and adjust portfolio, increase contributions, explore opportunities, and reassess health-related expenses.',
    },
    'year3': {
        'investment_recommendation': ['Bonds', 'Real Estate', 'Stocks'],
        'roadmap_to_achieve_goal': {
            'step1': {'action': 'Reevaluate goals and adjust strategy', 'risk_percentage': 20, 'success_percentage': 80},
            'step2': {'action': 'Consider divesting or rebalancing', 'risk_percentage': 25, 'success_percentage': 75},
            'step3': {'action': 'Ensure emergency fund', 'risk_percentage': 10, 'success_percentage': 90},
            'step4': {'action': 'Continue monitoring and adjusting portfolio', 'risk_percentage': 15, 'success_percentage': 85},
        },
        'savings_plan_health_issues': 'Evaluate and adjust health-related savings plan based on changes in health conditions and insurance coverage.',
        'summary': 'Reevaluate goals, consider divesting, ensure emergency fund, and evaluate health-related savings plan.',
    },
}

# Define background colors
def get_background_color(percentage):
    if percentage >= 50:
        return 'green'
    else:
        return 'red'

st.title('Financial Roadmap Visualization')

# Display Investment Recommendation
st.subheader('Investment Recommendation:')
st.write(', '.join(data['year1']['investment_recommendation']))

# Display Roadmap for each year
for year, details in data.items():
    # Expander for each year
    with st.expander(f'Year {year} - Click to Expand'):
        
        # Display Roadmap Steps
        st.subheader('Roadmap to Achieve Goals:')
        roadmap_step = details['roadmap_to_achieve_goal']
        for step, values in roadmap_step.items():
            risk_color = get_background_color(values["risk_percentage"])
            success_color = get_background_color(values["success_percentage"])
            
            st.markdown(
                f"<div style='margin:4px; background-color: {risk_color}; padding: 10px; border-radius: 5px; color: white; font-weight: 200;'>"
                f"{step}: {values['action']}</div>",
                unsafe_allow_html=True,
            )
            
            st.markdown(
                f"<div style='margin:4px; background-color: {success_color}; padding: 10px; border-radius: 5px; color: white; font-weight: 200;'>"
                f"Risk: {values['risk_percentage']}% | Success: {values['success_percentage']}%</div>",
                unsafe_allow_html=True,
            )

        # Display Savings Plan for Health Issues
        st.subheader('Savings Plan for Health Issues:')
        st.write(details['savings_plan_health_issues'])
        
        # Display Summary
        st.subheader('Summary:')
        st.write(details['summary'])
