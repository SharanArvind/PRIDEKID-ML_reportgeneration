class PRIDEModel:
    def __init__(self):
        pass

    def calculate_scores(self, accuracy, speed, consistency):
        mpi_score = (accuracy + speed + consistency) / 3
        mpi_growth_percentage = ((mpi_score - 7.5) / 7.5) * 100
        mpc = accuracy * ((2 * 30 - speed) / 30)
        return mpi_score, mpi_growth_percentage, mpc

    def classify_mpi_score(self, mpi_score):
        if mpi_score < 5:
            return "Gradually Potential"
        elif mpi_score < 10:
            return "Moderately Potential"
        elif mpi_score < 15:
            return "Steadily Potential"
        elif mpi_score < 20:
            return "Highly Potential"
        elif mpi_score < 25:
            return "Gradually Preparing"
        elif mpi_score < 30:
            return "Moderately Preparing"
        elif mpi_score < 35:
            return "Steadily Preparing"
        elif mpi_score < 40:
            return "Highly Preparing"
        elif mpi_score < 45:
            return "Gradually Promising"
        elif mpi_score < 50:
            return "Moderately Promising"
        elif mpi_score < 55:
            return "Steadily Promising"
        elif mpi_score < 60:
            return "Highly Promising"
        elif mpi_score < 65:
            return "Gradually Progressing"
        elif mpi_score < 70:
            return "Moderately Progressing"
        elif mpi_score < 75:
            return "Steadily Progressing"
        elif mpi_score < 80:
            return "Highly Progressing"
        elif mpi_score < 85:
            return "Gradually Performing"
        elif mpi_score < 90:
            return "Moderately Performing"
        elif mpi_score < 95:
            return "Steadily Performing"
        else:
            return "Highly Performing"

    def generate_report(self, name, accuracy, speed, consistency):
        mpi_score, mpi_growth_percentage, mpc = self.calculate_scores(accuracy, speed, consistency)
        classification = self.classify_mpi_score(mpi_score)

        # Detailed recommendations and content generation based on classification
        recommendations = {
            "Gradually Potential": "Focus on building a strong foundation in key areas.",
            "Moderately Potential": "Continue developing your skills to achieve steady progress.",
            "Steadily Potential": "Maintain your steady pace and seek opportunities for growth.",
            "Highly Potential": "You have high potential; aim to convert this into actionable outcomes.",
            "Gradually Preparing": "You're preparing well; focus on fine-tuning your skills.",
            "Moderately Preparing": "Your preparation is on track; keep refining your approach.",
            "Steadily Preparing": "Steady preparation is key; stay focused on your goals.",
            "Highly Preparing": "You're highly prepared; start applying your knowledge effectively.",
            "Gradually Promising": "Showcase your promise by consistently working towards your goals.",
            "Moderately Promising": "You're moderately promising; aim for consistent progress.",
            "Steadily Promising": "Steady promise is evident; keep pushing your boundaries.",
            "Highly Promising": "You show great promise; continue striving for excellence.",
            "Gradually Progressing": "Your progress is gradual; ensure you're moving in the right direction.",
            "Moderately Progressing": "Moderate progress is good; keep setting higher benchmarks.",
            "Steadily Progressing": "Your progress is steady; focus on maintaining your trajectory.",
            "Highly Progressing": "You are progressing well; aim to sustain and enhance your performance.",
            "Gradually Performing": "Gradual performance improvements are noticeable; keep at it.",
            "Moderately Performing": "You're performing well; strive to exceed expectations.",
            "Steadily Performing": "Steady performance is your strength; continue your efforts.",
            "Highly Performing": "You're performing at a high level; maintain and build upon this success."
        }

        report = f"""
        MPI Profile Report for {name}

        1. PRIDE Distribution
        Overall PRIDE Holistic Personality:
        - PRIDE Score: {mpi_score:.2f}
        - Classification: {classification}

        {recommendations[classification]}

        Daily PRIDE Process Works Polarity Order:
        1. Explaining intentions clearly
        2. Knowing details precisely
        3. Making wise decisions
        4. Solving problems effectively
        5. Building strong relationships

        2. Intelligence Distribution
        Daily Intelligence Outputs Polarity Order:
        1. Understanding the underlying concept/reason of the incident
        2. Altering the plans and actions based on situational needs/demands
        3. Following the appropriate process to complete the work

        3. PRIDE Skill Activities Polarity Level
        Top Activities:
        1. Conveying intentions with appropriate linguistics
        2. Remembering important info for future use
        3. Thinking out of the box or planning innovatively

        Areas for Improvement:
        - Internalizing life learnings with the right frame of mind
          - Grading: Weak, at Beginning Level
          - Causal Factors: Weak application of procedures on prioritizing, finding relevance
          - Skill Responsible: Mindset

        Detailed Description: Needs improvement in understanding feedback and criticism constructively.

        - Adapting well within a group for team synergy
          - Grading: Weak, at Beginning Level
          - Causal Factors: Less clarity on the advantages of adjusting in a team setup
          - Skill Responsible: Collaboration Ability

        Detailed Description: Needs improvement in team synergy and collaboration.

        - Delegating and guiding others respectfully
          - Grading: Weak, at Beginning Level
          - Causal Factors: Less clarity on the advantage of using leadership characteristics
          - Skill Responsible: Leadership Abilities

        Detailed Description: Needs improvement in leadership and delegation skills.

        4. Cognitive Performance
        - Accuracy: {accuracy}%
        - Speed: {speed}%
        - Consistency: {consistency}%

        5. Mental Productivity
        Productivity Profile:
        - Mental Performance Index (MPI) Score: {mpi_score:.2f}/10
        - MPI Growth Percentage: {mpi_growth_percentage:.2f}%
        - Mental Productivity Capacity (MPC): {mpc:.2f}%

        6. Mental Processing and Decision Making
        Mental Processing Speed:
        - Average time per question: {speed:.2f} seconds

        Appropriate Decision Consistency:
        - Consistency Ratio: 1:{(1.65 / (consistency / 100)):.2f}

        7. Ranking Order
        Daily PRIDE Skill Activities:
        1. Explaining intentions clearly
        2. Knowing details precisely
        3. Making wise decisions
        4. Solving problems effectively
        5. Building strong relationships

        PRIDE Skill Activities Improvement Focus:
        - Internalizing the life learnings with the right frame of mind
        - Adapting well within a group for team synergy
        - Delegating and guiding others respectfully

        8. Action Plan and Way Forward
        PRIDE: Influence Process
        - Work on decision-making processes by validating information based on motives, triggers, holistic benefits, process hurdles, and positive growth potential.

        Productivity: Accuracy
        - Focus on choosing the most appropriate responses to improve the quality of outcomes. Strive for accuracy in all work to ensure productivity is fruitful.

        Learning Styles: Read/Write
        - Enhance visualization skills when reading content by imagining it as a realistic incident or a movie. Understand the exact intention and emotions behind written words to improve comprehension.

        Intelligence: Fundamental Intelligence
        - Develop a deeper understanding of fundamental concepts, properties, procedures, and variations in all tasks. This knowledge will help in adapting to changes and leveraging opportunities effectively.

        Skill: Mindset
        - Cultivate a positive belief system that supports internalizing feedback and learning constructively. Validate information with appropriate criteria before applying it to new decisions.
        """
        return report
