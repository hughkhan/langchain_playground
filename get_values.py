import json
import os
from general_qa import get_answer_from_llm

traits = [
    {
        "name": "Intelligent",
        "description": "Intelligent"
    },
    {
        "name": "Creative",
        "description": "Creative"
    },
    {
        "name": "Innovative",
        "description": "Innovative"
    },
    {
        "name": "Analytical",
        "description": "Analytical"
    },
    {
        "name": "Logical",
        "description": "Logical"
    },
    {
        "name": "Practical",
        "description": "Practical"
    },
    {
        "name": "Technical",
        "description": "Technical"
    },
    {
        "name": "Open Minded",
        "description": "Open Minded"
    },
    {
        "name": "Adaptable",
        "description": "Adaptable"
    },
    {
        "name": "Humble",
        "description": "Humble"
    },
    {
        "name": "Resilient",
        "description": "Resilient"
    },
    {
        "name": "Empathetic",
        "description": "Empathetic"
    },
    {
        "name": "Collaborative",
        "description": "Collaborative"
    },
    {
        "name": "Communicative",
        "description": "Communicative"
    },
    {
        "name": "Leadership",
        "description": "Leadership"
    },
    {
        "name": "Influential",
        "description": "Influential"
    },
    {
        "name": "Motivational",
        "description": "Motivational"
    },
    {
        "name": "Inspiring",
        "description": "Inspiring"
    },
    {
        "name": "Visionary",
        "description": "Visionary"
    },
    {
        "name": "Strategic",
        "description": "Strategic"
    },
    {
        "name": "Organized",
        "description": "Organized"
    },
    {
        "name": "Efficient",
        "description": "Efficient"
    },
    {
        "name": "Detail Oriented",
        "description": "Detail Oriented"
    },
    {
        "name": "Quality Focused",
        "description": "Quality Focused"
    },
    {
        "name": "Customer Focused",
        "description": "Customer Focused"
    },
    {
        "name": "Service Oriented",
        "description": "Service Oriented"
    },
    {
        "name": "Positive",
        "description": "Positive"
    },
    {
        "name": "Optimistic",
        "description": "Optimistic"
    },
    {
        "name": "Enthusiastic",
        "description": "Enthusiastic"
    },
    {
        "name": "Passionate",
        "description": "Passionate"
    },
    {
        "name": "Honest",
        "description": "Honest"
    },
    {
        "name": "Transparent",
        "description": "Transparent"
    },
    {
        "name": "Ethical",
        "description": "Ethical"
    },
    {
        "name": "Responsible",
        "description": "Responsible"
    },
    {
        "name": "Accountable",
        "description": "Accountable"
    },
    {
        "name": "Dependable",
        "description": "Dependable"
    },
    {
        "name": "Reliable",
        "description": "Reliable"
    },
    {
        "name": "Consistent",
        "description": "Consistent"
    },
    {
        "name": "Punctual",
        "description": "Punctual"
    },
    {
        "name": "Dedicated",
        "description": "Dedicated"
    },
    {
        "name": "Committed",
        "description": "Committed"
    },
    {
        "name": "Loyal",
        "description": "Loyal"
    },
    {
        "name": "Trustworthy",
        "description": "Trustworthy"
    },
    {
        "name": "Feedback seeking",
        "description": "Feedback seeking"
    },
    {
        "name": "Self Aware",
        "description": "Self Aware"
    },
    {
        "name": "Self Regulated",
        "description": "Self Regulated"
    },
    {
        "name": "Self Motivated",
        "description": "Self Motivated"
    },
    {
        "name": "Self Disciplined",
        "description": "Self Disciplined"
    },
    {
        "name": "Self Confident",
        "description": "Self Confident"
    },
    {
        "name": "Self Reliant",
        "description": "Self Reliant"
    },
    {
        "name": "Self Sufficient",
        "description": "Self Sufficient"
    },
    {
        "name": "Self Directed",
        "description": "Self Directed"
    },
    {
        "name": "Conscientious",
        "description": "Conscientious"
    },
    {
        "name": "Nice",
        "description": "Nice"
    },
    {
        "name": "Polite",
        "description": "Polite"
    },
    {
        "name": "Caring",
        "description": "Caring"
    },
    {
        "name": "Kind",
        "description": "Kind"
    },
    {
        "name": "Generous",
        "description": "Generous"
    },
    {
        "name": "Empowering",
        "description": "Empowering"
    },
    {
        "name": "Supportive",
        "description": "Supportive"
    },
    {
        "name": "Encouraging",
        "description": "Encouraging"
    },
    {
        "name": "Nurturing",
        "description": "Nurturing"
    },
    {
        "name": "Mentoring",
        "description": "Mentoring"
    },
    {
        "name": "Coaching",
        "description": "Coaching"
    },
    {
        "name": "Outspoken",
        "description": "Outspoken"
    },
    {
        "name": "Assertive",
        "description": "Assertive"
    },
    {
        "name": "Decisive",
        "description": "Decisive"
    },
    {
        "name": "Peace seeking",
        "description": "Peace seeking"
    },
    {
        "name": "Conflict resolving",
        "description": "Conflict resolving"
    },
    {
        "name": "Consiliatory",
        "description": "Consiliatory"
    },
    {
        "name": "grateful",
        "description": "grateful"
    },
    {
        "name": "Appreciative",
        "description": "Appreciative"
    },
    {
        "name": "Thankful",
        "description": "Thankful"
    },
    {
        "name": "Gracious",
        "description": "Gracious"
    },
    {
        "name": "Forgiving",
        "description": "Forgiving"
    },
    {
        "name": "Understanding",
        "description": "Understanding"
    },
    {
        "name": "Patient",
        "description": "Patient"
    },
    {
        "name": "Tolerant",
        "description": "Tolerant"
    },
    {
        "name": "Accepting",
        "description": "Accepting"
    },
    {
        "name": "Confident",
        "description": "Confident"
    },
    {
        "name": "Courageous",
        "description": "Courageous"
    },
    {
        "name": "Bold",
        "description": "Bold"
    },
    {
        "name": "Fearless",
        "description": "Fearless"
    },
    {
        "name": "Grounded",
        "description": "Grounded"
    },
    {
        "name": "Balanced",
        "description": "Balanced"
    },
    {
        "name": "Stable",
        "description": "Stable"
    },
    {
        "name": "Friendly",
        "description": "Friendly"
    },
    {
        "name": "Sociable",
        "description": "Sociable"
    },
    {
        "name": "Outgoing",
        "description": "Outgoing"
    },
    {
        "name": "High Emotional Quotient",
        "description": "High Emotional Quotient"
    },
    {
        "name": "High Social Quotient",
        "description": "High Social Quotient"
    },
    {
        "name": "High Cultural Quotient",
        "description": "High Cultural Quotient"
    },
    {
        "name": "High Spiritual Quotient",
        "description": "High Spiritual Quotient"
    },
    {
        "name": "High Moral Quotient",
        "description": "High Moral Quotient"
    },
    {
        "name": "High Ethical Quotient",
        "description": "High Ethical Quotient"
    },
    {
        "name": "High Integrity Quotient",
        "description": "High Integrity Quotient"
    },
    {
        "name": "High Intellectual Quotient",
        "description": "High Intellectual Quotient"
    },
    {
        "name": "Tactful",
        "description": "Tactful"
    },
    {
        "name": "Diplomatic",
        "description": "Diplomatic"
    },
    {
        "name": "Cultured",
        "description": "Cultured"
    },
    {
        "name": "Sophisticated",
        "description": "Sophisticated"
    },
    {
        "name": "Well Mannered",
        "description": "Well Mannered"
    },
    {
        "name": "Well Behaved",
        "description": "Well Behaved"
    },
    {
        "name": "Selfless",
        "description": "Selfless"
    },
    {
        "name": "Altruistic",
        "description": "Altruistic"
    },
    {
        "name": "Philanthropic",
        "description": "Philanthropic"
    },
    {
        "name": "Empathetic",
        "description": "Empathetic"
    },
    {
        "name": "Compassionate",
        "description": "Compassionate"
    },
    {
        "name": "Sympathetic",
        "description": "Sympathetic"
    },
    {
        "name": "Kind Hearted",
        "description": "Kind Hearted"
    },
    {
        "name": "Warm",
        "description": "Warm"
    },
    {
        "name": "Gentle",
        "description": "Gentle"
    },
    {
        "name": "Soft Spoken",
        "description": "Soft Spoken"
    },
    {
        "name": "Precise",
        "description": "Precise"
    },
    {
        "name": "Accurate",
        "description": "Accurate"
    },
    {
        "name": "Meticulous",
        "description": "Meticulous"
    },
    {
        "name": "Thorough",
        "description": "Thorough"
    },
    {
        "name": "Systematic",
        "description": "Systematic"
    },
    {
        "name": "Methodical",
        "description": "Methodical"
    },
    {
        "name": "Organized",
        "description": "Organized"
    },
    {
        "name": "Efficient",
        "description": "Efficient"
    },
    {
        "name": "Resourceful",
        "description": "Resourceful"
    },
    {
        "name": "Calm",
        "description": "Calm"
    },
    {
        "name": "Cool",
        "description": "Cool"
    },
    {
        "name": "Collected",
        "description": "Collected"
    },
    {
        "name": "Composed",
        "description": "Composed"
    },
    {
        "name": "Serene",
        "description": "Serene"
    },
    {
        "name": "Tranquil",
        "description": "Tranquil"
    },
    {
        "name": "Relaxed",
        "description": "Relaxed"
    },
    {
        "name": "Unflappable",
        "description": "Unflappable"
    },
    {
        "name": "Unruffled",
        "description": "Unruffled"
    },
    {
        "name": "Curious",
        "description": "Curious"
    },
    {
        "name": "Inquisitive",
        "description": "Inquisitive"
    },
    {
        "name": "Explorative",
        "description": "Explorative"
    },
    {
        "name": "Investigative",
        "description": "Investigative"
    },
    {
        "name": "Perceptive",
        "description": "Perceptive"
    },
    {
        "name": "Observant",
        "description": "Observant"
    },
    {
        "name": "Insightful",
        "description": "Insightful"
    },
    {
        "name": "Intuitive",
        "description": "Intuitive"
    },
    {
        "name": "Aware",
        "description": "Aware"
    },
    {
        "name": "Mindful",
        "description": "Mindful"
    },
    {
        "name": "Present",
        "description": "Present"
    },
    {
        "name": "Focused",
        "description": "Focused"
    },
    {
        "name": "Attentive",
        "description": "Attentive"
    },
    {
        "name": "Concentrated",
        "description": "Concentrated"
    },
    {
        "name": "Engaged",
        "description": "Engaged"
    },
    {
        "name": "Involved",
        "description": "Involved"
    },
    {
        "name": "Participative",
        "description": "Participative"
    },
    {
        "name": "Interactive",
        "description": "Interactive"
    },
    {
        "name": "Good sense of Humor",
        "description": "Good sense of Humor"
    },
    {
        "name": "Witty",
        "description": "Witty"
    },
    {
        "name": "Clever",
        "description": "Clever"
    },
    {
        "name": "Sharp",
        "description": "Sharp"
    },
    {
        "name": "Quick",
        "description": "Quick"
    },
    {
        "name": "Fast",
        "description": "Fast"
    },
    {
        "name": "Bright",
        "description": "Bright"
    },
    {
        "name": "Open-minded",
        "description": "Open-minded"
    },
    {
        "name": "Progressive",
        "description": "Progressive"
    },
    {
        "name": "Forward thinking",
        "description": "Forward thinking"
    },
    {
        "name": "Purposeful",
        "description": "Purposeful"
    },
    {
        "name": "Goal oriented",
        "description": "Goal oriented"
    },
    {
        "name": "Driven",
        "description": "Driven"
    },
    {
        "name": "Ambitious",
        "description": "Ambitious"
    },
    {
        "name": "Motivated",
        "description": "Motivated"
    },
    {
        "name": "Inspired",
        "description": "Inspired"
    },
    {
        "name": "Objective",
        "description": "Objective"
    },
    {
        "name": "Fair",
        "description": "Fair"
    },
    {
        "name": "Impartial",
        "description": "Impartial"
    },
    {
        "name": "Just",
        "description": "Just"
    },
    {
        "name": "Equitable",
        "description": "Equitable"
    },
    {
        "name": "Unbiased",
        "description": "Unbiased"
    },
    {
        "name": "Prudent",
        "description": "Prudent"
    },
    {
        "name": "Sensible",
        "description": "Sensible"
    },
    {
        "name": "Reasonable",
        "description": "Reasonable"
    },
    {
        "name": "Pragmatic",
        "description": "Pragmatic"
    },
    {
        "name": "Realistic",
        "description": "Realistic"
    },
    {
        "name": "Logical",
        "description": "Logical"
    },
    {
        "name": "Rational",
        "description": "Rational"
    },
    {
        "name": "Analytical",
        "description": "Analytical"
    },
    {
        "name": "Likable",
        "description": "Likable"
    },
    {
        "name": "Charming",
        "description": "Charming"
    },
    {
        "name": "Theoretical",
        "description": "Theoretical"
    },
    {
        "name": "Philosophical",
        "description": "Philosophical"
    },
    {
        "name": "Intellectual",
        "description": "Intellectual"
    },
    {
        "name": "Discriminating",
        "description": "Discriminating"
    },
    {
        "name": "Admired",
        "description": "Admired"
    },
    {
        "name": "Respected",
        "description": "Respected"
    },
    {
        "name": "Esteemed",
        "description": "Esteemed"
    },
    {
        "name": "Honored",
        "description": "Honored"
    },
    {
        "name": "Valued",
        "description": "Valued"
    },
    {
        "name": "Appreciated",
        "description": "Appreciated"
    },
    {
        "name": "affectionate",
        "description": "affectionate"
    },
    {
        "name": "Warm-hearted",
        "description": "Warm-hearted"
    },
    {
        "name": "Devoted",
        "description": "Devoted"
    },
    {
        "name": "Attentive",
        "description": "Attentive"
    },
    {
        "name": "Considerate",
        "description": "Considerate"
    },
    {
        "name": "Thoughtful",
        "description": "Thoughtful"
    },
    {
        "name": "Not bivalent",
        "description": "Not bivalent"
    },
    {
        "name": "Competent",
        "description": "Competent"
    },
    {
        "name": "Capable",
        "description": "Capable"
    },
    {
        "name": "Able",
        "description": "Able"
    },
    {
        "name": "Skilled",
        "description": "Skilled"
    },
    {
        "name": "Talented",
        "description": "Talented"
    },
    {
        "name": "Gifted",
        "description": "Gifted"
    },
    {
        "name": "Expert",
        "description": "Expert"
    },
    {
        "name": "Specialist",
        "description": "Specialist"
    },
    {
        "name": "Professional",
        "description": "Professional"
    },
    {
        "name": "Well-informed",
        "description": "Well-informed"
    },
    {
        "name": "Knowledgeable",
        "description": "Knowledgeable"
    },
    {
        "name": "Wise",
        "description": "Wise"
    },
    {
        "name": "Smart",
        "description": "Smart"
    },
    {
        "name": "Conforming",
        "description": "Conforming"
    },
    {
        "name": "Compliant",
        "description": "Compliant"
    },
    {
        "name": "Egalitarian",
        "description": "Egalitarian"
    },
    {
        "name": "Fair-minded",
        "description": "Fair-minded"
    },
    {
        "name": "Mastery Seeking",
        "description": "Mastery Seeking"
    },
    {
        "name": "Self-actualized",
        "description": "Self-actualized"
    },
    {
        "name": "Independent thinker",
        "description": "Independent thinker"
    },
    {
        "name": "Problem Solver",
        "description": "Problem Solver"
    },
    {
        "name": "Persuasive",
        "description": "Persuasive"
    },
    {
        "name": "Influential",
        "description": "Influential"
    },
    {
        "name": "Charismatic",
        "description": "Charismatic"
    },
    {
        "name": "Unity Seeking",
        "description": "Unity Seeking"
    },
    {
        "name": "Collaborative",
        "description": "Collaborative"
    }
]

Values = [
    {
        "name": "Innovation",
        "description": "Add Later"
    },
    {
        "name": "Customer-Centricity",
        "description": "Add Later"
    },
    {
        "name": "Excellence",
        "description": "Add Later"
    },
    {
        "name": "Accountability",
        "description": "Add Later"
    },
    {
        "name": "Collaboration",
        "description": "Add Later"
    },
    {
        "name": "Respect",
        "description": "Add Later"
    },
    {
        "name": "Diversity",
        "description": "Add Later"
    },
    {
        "name": "Sustainability",
        "description": "Add Later"
    },
    {
        "name": "Transparency",
        "description": "Add Later"
    },
    {
        "name": "Continuous Improvement",
        "description": "Add Later"
    },
    {
        "name": "Passion",
        "description": "Add Later"
    },
    {
        "name": "Adaptability",
        "description": "Add Later"
    },
    {
        "name": "Trustworthiness",
        "description": "Add Later"
    },
    {
        "name": "Teamwork",
        "description": "Add Later"
    },
    {
        "name": "Courage",
        "description": "Add Later"
    },
    {
        "name": "Fairness",
        "description": "Add Later"
    },
    {
        "name": "Professionalism",
        "description": "Add Later"
    },
    {
        "name": "Social Responsibility",
        "description": "Add Later"
    },
    {
        "name": "Openness",
        "description": "Add Later"
    },
    {
        "name": "Quality",
        "description": "Add Later"
    },
    {
        "name": "Learning",
        "description": "Add Later"
    },
    {
        "name": "Efficiency",
        "description": "Add Later"
    },
    {
        "name": "Ethical Behavior",
        "description": "Add Later"
    },
    {
        "name": "Humility",
        "description": "Add Later"
    },
    {
        "name": "Boldness",
        "description": "Add Later"
    },
    {
        "name": "Loyalty",
        "description": "Add Later"
    },
    {
        "name": "Responsiveness",
        "description": "Add Later"
    },
    {
        "name": "Growth",
        "description": "Add Later"
    },
    {
        "name": "Simplicity",
        "description": "Add Later"
    },
    {
        "name": "Wellness",
        "description": "Add Later"
    },
    {
        "name": "Inclusivity",
        "description": "Add Later"
    },
    {
        "name": "Entrepreneurial Spirit",
        "description": "Add Later"
    },
    {
        "name": "Flexibility",
        "description": "Add Later"
    },
    {
        "name": "Selflessness",
        "description": "Add Later"
    },
    {
        "name": "Purposefulness",
        "description": "Add Later"
    },
    {
        "name": "Humor",
        "description": "Add Later"
    },
    {
        "name": "Systems Thinking",
        "description": "Add Later"
    },
    {
        "name": "Customer Value",
        "description": "Add Later"
    },
    {
        "name": "Communication",
        "description": "Add Later"
    },
    {
        "name": "Self-direction",
        "description": "Add Later"
    },
    {
        "name": "Objectivity",
        "description": "Add Later"
    },
    {
        "name": "Responsibility",
        "description": "Add Later"
    },
    {
        "name": "Egalitarianism",
        "description": "Add Later"
    },
    {
        "name": "Team Spirit",
        "description": "Add Later"
    },
    {
        "name": "Positivity",
        "description": "Add Later"
    },
    {
        "name": "Grit",
        "description": "Add Later"
    },
    {
        "name": "Conscientiousness",
        "description": "Add Later"
    },
    {
        "name": "Curiosity",
        "description": "Add Later"
    },
    {
        "name": "Nurture",
        "description": "Add Later"
    },
    {
        "name": "Cultural Fit",
        "description": "Add Later"
    },
    {
        "name": "Open-mindedness",
        "description": "Add Later"
    },
    {
        "name": "Risk-taking",
        "description": "Add Later"
    },
    {
        "name": "Dedication",
        "description": "Add Later"
    },
    {
        "name": "Mastery",
        "description": "Add Later"
    },
    {
        "name": "Tenacity",
        "description": "Add Later"
    }
]




def get_value_description():
    try:

        # for item in data:
        #     item["description"] = get_answer_from_llm(f"Give the definition, in less than 60 words, of the following English description as it is " \
        #                                               "applied to an employee of a business. The answer should be in unformatted text form:", 
        #                                               item["name"])
        #     print(item["name"] + ":  " + item["description"])

        # output_file = r'/mnt/c/users/Humay/OneDrive/froid/Technical/full1.json'

        # with open(output_file, 'w') as outfile:
        #     json.dump(data, outfile, indent=4)

        for item in Values:
            item["description"] = get_answer_from_llm(f"Give the definition, in less than 60 words, of the following English term as it describes " \
                                                      "a corporate value adopted by a business. The answer should be in unformatted text form:", 
                                                      item["name"])
            print(item["name"] + ":  " + item["description"])

        output_file = r'/mnt/c/users/Humay/OneDrive/froid/Technical/full_values1.json'

        with open(output_file, 'w') as outfile:
            json.dump(Values, outfile, indent=4)        

    except Exception as e:
        print(f"An error occurred: {e}")
    
