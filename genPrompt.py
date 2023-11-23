class TransPrompt:
    def __init__(self) -> None:
        self.basePrompt="""
        
        Given the graphical data provided, analyze the columns and provide essential insights.
        the graphical data is present in the form of python dictionary,
        consider the detials for follwing inputs:
        """

    def getCreditDebitSummaryPrompt(self,credit_details,debit_details,period=1):
        self.prompt=f"""
        The below numerical data is present in the form of a python dictionary, representing credit and debit details for {period} month:
        {credit_details},
        {debit_details},
        provide the insights for above details, includes only foll0wing formatted output, do not explain it in more depth just calculate it and provide
        [income rate,expenditure rate, net loss/profit,percentage of income to expenditure]
        and at end provide me 2 -3 lines summary including important suggetions to grow income and reduce expenditure
        
        """

        return self.basePrompt+self.prompt
    
    def getCategoryAnalysisPrompt(self,period,catdict,type):
        self.prompt=f"""
        Below given is the csv data representing the category wise analysis for {period} month,
        {catdict}
        Give me the insights of this analysis that includes maximum {type}ed for which category, minimum {type}ed for which category and which category will help me to generate maximum credit or which category is increasing my expenditure? 
        and at end provide 2-4 lines suggestion about Category wise analysis 
        """
        return self.basePrompt+self.prompt
    
    def getMerchantAnalysisPrompt(self,period,merchDict,type):
        self.prompt=f"""
        
        Below numerical data represent the merchants that involved in process of transaction for {period} month,
        {merchDict}
        provide the insights for above details by analyzing given data, includes only following formatted output, do not explain it in more depth just predict it and provide 
        for {type} transactions: [maximum transaction {type}ed for which merchant?, minimum transaction {type}ed for which merchant?, which merchant help to generate maximum credit or which merchant is increasing expenditure?]
        and at end provide 2-4 lines suggestion about merchant analysis 
        
        """
        return str(self.basePrompt+self.prompt)
    def getLocAnalysisPrompt(self,period,locDict,type):
        self.prompt=f"""
        Below numerical data represent the location wise transaction happend that involved in process of transaction for {period} month,
        {locDict}
        
        provide the insights for above details by analyzing given data, includes only following formatted output, do not explain it in more depth just predict it and provide 
        for {type} transactions: [maximum transaction {type}ed form which city?, minimum transaction {type}ed form which city?, which city is have average transaction?]


        and at end provide 2-4 lines suggestion about location wise analysis of transaction 
        """

        return self.basePrompt+self.prompt
    
    def getPaymentMethodAnalysisPrompt(self,period,payMtdDict,type):
        self.prompt=f"""
        Below numerical data represent the payment method used while doing transaction happend that involved in process of transaction for {period} month,
        {payMtdDict}
        
        provide the insights for above details by analyzing given data, includes only following formatted output, do not explain it in more depth just predict it and provide 
        for {type} transactions: [maximum transaction {type}ed by which payment method?, minimum transaction {type}ed by which payment method?, which payment method is most suitable for user?]
        and at end provide 2-4 lines suggestion about payment method usage to improve transactions
        """

        return self.basePrompt+self.prompt

    def getStatAnalysisPrompt(self,statDict,period=1):
        self.prompt=f"""
        Below is Statistical majors of {period} month analysis, analyse it in depth and get the valuable insights

        dataset :
        {statDict}
        
        provide the insights for above Statistical measures, include only follwing formatted output, do not expalain it in depth, just be specific with your answer
        what each statistic say in one line of each.

        finally, provide suggestion to improve income and be financial stable
        Also start with some greetings!
        """

        return self.basePrompt+self.prompt
    
    


class GoalPlanner:
    def __init__(self) -> None:
        self.container=[]
    
    def getGoalPromptBaseTemplate(self,financialBackground,financialGoals,investmentPreference,healthConsideration='',savingHabits='',lifestyleAndPreference='',experienceInInvestments='',futureIncomeStreams='',knowledgeEducation='',legalAndFamilyConsiderations=''):
        self.prompt=f"""
        user background details represented as python dictionary:
        \n{financialBackground},
        \n{financialGoals},
        \n{investmentPreference},
        \n{healthConsideration},
        \n{savingHabits},
        \n{lifestyleAndPreference},
        \n{experienceInInvestments},
        \n{futureIncomeStreams},
        \n{knowledgeEducation},
        \n{legalAndFamilyConsiderations}

    
        consider the user's responses to the above question and their past transaction details. Generate a comprehensive roadmap that includes the following:
        -- investment recommendations based on their financial goals and risk tolerance.
        -- savings plan suggestions, considering any health issues mentioned.
        -- clear steps with predicted risk percentage and success percentage for the user to follow.
        -- provide explanations for the recommendations to enhance user understanding.


        provide the output formatted as follows and do not include extra depth, make is specific, and easy to understand:
        {{
            'year1':{{
                'investment recommendation':'prioprity wise recommendations',
                'roadmap to achieve one of the best goal':'indetail roadmap with risk percentage and success percentage',
                'savings plan if any health issues':'Guide for better savings plan based on user profile',
                'summary':'make above things with clear perception'
                }}
        }}

        do this for 3 year goal planing and keep keys of nested dictionary i.e 'retirment recommendation' and other same, do povide suggestion in value of dictionary.
        
        """
        return self.prompt
    

class stockMarketAdvisor:
    def __init__(self) -> None:
        pass


if __name__=='__main__':
    obj=TransPrompt()
    cd={'credit': {
        'total_credit_amount': 12000,
        'num_credit_transactions': 50,
        'avg_credit_amount': 2987,
        'income_from_sources': 4500
    }
    }
    dd={
        'debit': {
        'total_debit_amount': 15000,
        'num_debit_transactions': 80,
        'avg_debit_amount': 800,
        'expenditure_for_month': 8000
    }
    }

    prompt=obj.getCreditDebitSummaryPrompt(period=1,credit_details=cd,debit_details=dd)
    print(prompt)