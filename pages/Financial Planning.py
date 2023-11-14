import streamlit as st
import genPrompt
import genAiUtils
gp=genPrompt.GoalPlanner()
gpt=genAiUtils.gptLLM('')
def financial_background_section():
    with st.expander("Financial Background:"):
        current_income = st.number_input("What is your current income level?")
        monthly_expenses = st.number_input("Can you provide details about your monthly expenses?")
        outstanding_debts = st.checkbox("Do you have any outstanding debts or loans?")
        credit_score = st.number_input("What is your credit score?")

        return {
        "current_income": current_income,
        "monthly_expenses": monthly_expenses,
        "outstanding_debts": outstanding_debts,
        "credit_score": credit_score
        }

def financial_goals_section():
    with st.expander("Financial Goals:"):
        short_term_goals = st.text_area("What are your short-term financial goals (within the next 1-3 years)?")
        long_term_goals = st.text_area("What are your long-term financial goals (beyond 3 years)?")
        specific_purpose = st.text_area("Are you saving for a specific purpose, such as education, a home, or retirement?")

        return {
        "short_term_goals": short_term_goals,
        "long_term_goals": long_term_goals,
        "specific_purpose": specific_purpose
        }

def investment_preferences_section():
    with st.expander("Investment Preferences:"):
        risk_tolerance = st.selectbox("How would you describe your risk tolerance?", ["Low", "Medium", "High"])
        investment_strategy = st.selectbox("Are you interested in conservative, balanced, or aggressive investment strategies?", ["Conservative", "Balanced", "Aggressive"])
        investment_types = st.multiselect("Do you have any preferences regarding specific types of investments?", ["Stocks", "Bonds", "Real Estate"])

        return {
        "risk_tolerance": risk_tolerance,
        "investment_strategy": investment_strategy,
        "investment_types": investment_types
        }

def health_considerations_section():
    with st.expander("Health Consideratons"):
        health_conditions=st.checkbox("Do you have any existing health conditions that may impact your financial planning?")
        anticipated_health_expenses_in_future   =st.checkbox('Are there anticipated health-related expenses in the near future?')     
        health_insurance_coverage=st.checkbox("Do you have health insurance coverage?")

        return{
            "health_conditions":health_conditions,
            "anticipated_health_expenses_in_future":anticipated_health_expenses_in_future,
            "health_insurance_coverage":health_insurance_coverage
        }


def savingHabits_section():
    with st.expander("Saving Details"):
        monthly_saving_or_invest=st.number_input('How much do you currently save or invest each month?')
        emergency_fun_available=st.checkbox("Do you have an emergency fund, and if so, how much is in it?")
        comfortable_with_long_term_investment=st.checkbox("Are you comfortable with the idea of long-term savings and investments?")

        return {
            "monthly_saving_or_invest":monthly_saving_or_invest,
            "emergency_fun_available":emergency_fun_available,
            "comfortable_with_long_term_investment":comfortable_with_long_term_investment
        }


def lifeStyleAndPreferences_section():
    with st.expander("Lifestyle and Preferences"):
        impact_of_life_stlye_on_financial_decisions=st.checkbox('What is your preferred lifestyle, and how does it impact your financial decisions?')
        any_preferences_or_values_considered_in_financial_planing=st.checkbox("Do you have any specific preferences or values that should be considered in financial planning?")

        return {
            "impact_of_life_stlye_on_financial_decisions":impact_of_life_stlye_on_financial_decisions,
            "any_preferences_or_values_considered_in_financial_planing":any_preferences_or_values_considered_in_financial_planing
        }

def experienceInvestments_section():
    with st.expander("Experience with investments"):
        financial_invest_yr=st.number_input("Have you invested in the financial markets before? If so, what was your experience?")
        specific_pref_invest=st.checkbox('Do you have any specific preferences regarding ethical or sustainable investments?')

        return {
            "number_of_years_experience_in_financial_investment":financial_invest_yr,
            "specifi_preferences_regrading_sustainable_investment":specific_pref_invest
        }    

def futureIncomeStreams_section():
    with st.expander("Future Income Stream"):
        change_in_income=st.checkbox("Are you anticipating any changes in your income in the near future (job changes, promotions, etc.)?")    
        
        return {
            "anticipating any changes in your income in the near future":change_in_income
        }

def knowledgeEdu_section():
    with st.expander("Knowledge and Education"):
        financial_literacy_rate=st.number_input("How would you rate your financial literacy?(out of 10)")
        interested_in_learning=st.checkbox("Are you interested in learning more about financial planning and investments?")
        
        return {
            "financial literacy rate out of 10.00":financial_literacy_rate,
            "interested in learning about financial planning":interested_in_learning
        }
    
    
def familyConsiderations_section():
    with st.expander("Legal and Family Considerations"):
        dependency=st.checkbox("Do you have dependents, and how does this factor into your financial planning?")
        legal_constraints=st.checkbox("Are there any legal constraints or obligations that should be considered?")

        return {
            "any dependency factor (family or legal) into your financial planning":dependency,
            "legal constraints or obligations should be consided in planning":legal_constraints
        }
    

def main():
    st.title("Financial Planning Servey")

    financial_background = financial_background_section()
    financial_goals = financial_goals_section()
    investment_preferences = investment_preferences_section()
    health_considerations=health_considerations_section()
    savingHabits=savingHabits_section()
    lifeStyleAndPreferences=lifeStyleAndPreferences_section()
    experienceInvestments=experienceInvestments_section()
    futureIncomeStreams=futureIncomeStreams_section()
    knowledgeEdu=knowledgeEdu_section()
    familyConsiderations=familyConsiderations_section()

    # Display collected information
    # st.subheader("Collected Information:")
    # st.write("Financial Background:", financial_background)
    # st.write("Financial Goals:", financial_goals)
    # st.write("Investment Preferences:", investment_preferences)

    # submit the form 
    if st.button("Build Road Map"):
        # combine all collected informatino to generate prompt
        prompt=gp.getGoalPromptBaseTemplate(financialBackground=financial_background,financialGoals=financial_goals,investmentPreference=investment_preferences,healthConsideration=health_considerations,savingHabits=savingHabits,experienceInInvestments=experienceInvestments,futureIncomeStreams=futureIncomeStreams,knowledgeEducation=knowledgeEdu,legalAndFamilyConsiderations=familyConsiderations,lifestyleAndPreference=lifeStyleAndPreferences)
        st.header("Prompt Generated")
        st.write(gpt.generate_response(prompt))

    
    if st.button('Clear'):
        # reset all the input fields 
        st.rerun()
        
if __name__ == "__main__":
    main()
