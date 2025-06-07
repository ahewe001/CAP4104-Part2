import streamlit as st
import pandas as pd


def question(df, key):
    #grabing question, options, correct answer, and explanation from df at row "key"
    row = df.iloc[key]
    options = [row["opt_1"], row["opt_2"], row["opt_3"], row["opt_4"]]
    correct_answer = row["correct_answer"]
    expln = row["explanation"]
    form = st.form(key=f"quiz_form{key}")

    #creating a form with question and radio
    with form:
        user_choice = form.radio(row["question"], options, key=f"radio_{key}")
        submitted = form.form_submit_button("Submit")

    #if user submitted and it's the right answer, function returns true, else returns false. returns expln for both
    if submitted:
        if user_choice == correct_answer:
            return True, expln
        else:
            return False, expln
    return None, None


def quiz_questions():
    #opening csv located in files
    df = pd.read_csv("question_bank.csv")
    #num of questions to pull from csv
    q_amt = 3

    #for the user's name
    if "name" not in st.session_state:
        st.session_state.name = ""
    #for keeping score
    if "score" not in st.session_state:
        st.session_state.score = 0
    #for the index of the question
    if "q_index" not in st.session_state:
        st.session_state.q_index = 0
    #initial df of shuffled questions bank
    if "shuffled_df" not in st.session_state:
        st.session_state.shuffled_df = df.sample(frac=1).reset_index(drop=True)
    #subset of the shuffled questions bank
    if "df_subset" not in st.session_state:
        st.session_state.df_subset = st.session_state.shuffled_df.iloc[:q_amt]
    #for showing result -> did user submit answer? if so, TRUE
    if "show_result" not in st.session_state:
        st.session_state.show_result = False
    #keep track of user answer, true or false from quiz function return
    if "last_answer_correct" not in st.session_state:
        st.session_state.last_answer_correct = None
    #explaination of the correct answer
    if "last_expln" not in st.session_state:
        st.session_state.last_expln = ""
    #check box to make sure user checked for score
    if "check_box" not in st.session_state:
        st.session_state.check_box = False

    #put name and check box for score keeping
    text = st.text_input("Enter your name and check the box if you want to count your score.")
    st.session_state.name = text
    st.session_state.check_box = st.checkbox("Count my score!")

    #shortcut
    q_index = st.session_state.q_index

    # while the index is less than the question amount
    if q_index < q_amt:
        #result and explanation from the question found in df_subset at q_index
        result, expln = question(st.session_state.df_subset, q_index)

        #if user submitted then
        if result is not None:
            #we will show_result as TRUE, save the result (would be TRUE or FALSE) and the explanation of the question
            st.session_state.show_result = True
            st.session_state.last_answer_correct = result
            st.session_state.last_expln = expln
            if result:
                #is result true? Add to score if check box checked
                if st.session_state.check_box:
                    st.session_state.score += 1

        #did user submit answer?
        if st.session_state.show_result:
            if st.session_state.last_answer_correct:
                # last_answer = true in previous if statement
                st.success(":tada: Correct!")
            else:
                # last_answer = false in previous if statement
                st.error(":x: Wrong Answer!")
            #explanation will be written for both wrong and right answers
            st.write(st.session_state.last_expln)

            #next question button with unique key, will increase q_index and make show_result false again
            #button will restart script with updated changes
            if st.button("Next Question", key=f"next_{q_index}"):
                st.session_state.q_index += 1
                st.session_state.show_result = False
                #code doesn't immediately rerun with new index so streamlit in turn is
                #rendering with same index until next refresh so st.rerun() necessary to prevent sticky button
                st.rerun()

    #q_index reached question amount
    else:
        st.write(f":tada: Congratulations {st.session_state.name}, you've completed the quiz!")
        if st.session_state.check_box:
            st.write(f"Your final score: **{st.session_state.score}/{q_amt}**")




