def chatbot_response(user_input):
    user_input = user_input.lower()

    health_data = {
        "fever": (
            "Fever may indicate an infection or inflammation in the body.\n"
            "Make sure to drink plenty of fluids, take proper rest, and monitor your temperature regularly.\n"
            "If the fever lasts more than 2 days or exceeds 101°F, please consult a doctor."
        ),

        "cold": (
            "The common cold is usually caused by a viral infection.\n"
            "Take proper rest, drink warm fluids, and avoid cold drinks.\n"
            "If symptoms persist for more than 3 days, consult a healthcare professional."
        ),

        "cough": (
            "A cough may be caused by infection, allergy, or irritation.\n"
            "Drink warm water, avoid cold foods, and take steam inhalation.\n"
            "If the cough lasts more than a week, consult a doctor."
        ),

        "headache": (
            "Headaches are commonly caused by stress, dehydration, or lack of sleep.\n"
            "Drink enough water, take short breaks from screens, and rest properly.\n"
            "If headaches occur frequently, please consult a doctor."
        ),

        "diabetes": (
            "Diabetes is a condition where blood sugar levels remain high.\n"
            "Maintain a balanced diet, exercise regularly, and monitor your sugar levels.\n"
            "Regular medical checkups are important to prevent complications."
        ),

        "blood pressure": (
            "High blood pressure increases the risk of heart disease and stroke.\n"
            "Reduce salt intake, exercise daily, and manage stress properly.\n"
            "Regular BP monitoring and doctor consultation is recommended."
        ),

        "stress": (
            "Stress can affect both mental and physical health.\n"
            "Practice meditation, deep breathing, and maintain a healthy routine.\n"
            "If stress becomes overwhelming, seek professional support."
        ),

        "anxiety": (
            "Anxiety can cause restlessness, worry, and difficulty concentrating.\n"
            "Try relaxation techniques, breathing exercises, and regular physical activity.\n"
            "If anxiety affects daily life, consult a mental health professional."
        ),

        "sleep": (
            "Good sleep is essential for overall health and immunity.\n"
            "Try to sleep 7–8 hours daily and maintain a regular sleep schedule.\n"
            "Avoid screen usage before bedtime for better sleep quality."
        )
    }

    for key in health_data:
        if key in user_input:
            return health_data[key]

    return (
        "Please provide more details about your health concern.\n"
        "I can help with symptoms, lifestyle advice, and basic health guidance.\n"
        "For serious conditions, always consult a qualified medical professional."
    )
