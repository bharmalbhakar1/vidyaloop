import streamlit as st
import re

# Set page layout configuration to wide mode to emulate a professional dashboard
st.set_page_config(page_title="Vidyaloop - Student Personality Assessment", layout="wide", initial_sidebar_state="collapsed")

# =====================================================================
# 1. APPLICATION DATA & SCORING MATRICES
# =====================================================================
# Threshold definitions mapping total scores to tier categories
SCORE_THRESHOLDS = {
    "confidence": {"low": (5, 11), "medium": (12, 18), "high": (19, 30)},
    "self_awareness": {"low": (6, 13), "medium": (14, 22), "high": (23, 30)},
    "decision_making": {"low": (6, 13), "medium": (14, 22), "high": (23, 30)},
    "emotional_balance": {"low": (6, 13), "medium": (14, 22), "high": (23, 30)},
    "drive": {"low": (6, 13), "medium": (14, 22), "high": (23, 30)}
}

# The 30 core evaluation questions mapped to their active dimensions
QUESTIONS = [
    {"id": 1, "text": "I speak up in class or group discussions even when I am not fully sure of my answer.", "dim": "confidence", "reverse": False},
    {"id": 2, "text": "I feel comfortable sharing my opinions with others.", "dim": "confidence", "reverse": False},
    {"id": 3, "text": "I can start or continue conversations without feeling too nervous.", "dim": "confidence", "reverse": False},
    {"id": 4, "text": "I participate actively when working in teams or groups.", "dim": "confidence", "reverse": False},
    {"id": 5, "text": "I avoid speaking in front of others because I fear being judged.", "dim": "confidence", "reverse": True},
    {"id": 6, "text": "I often stay quiet even when I have something important to say.", "dim": "confidence", "reverse": True},
    
    {"id": 7, "text": "I understand what my strengths are in studies, activities, or daily life.", "dim": "self_awareness", "reverse": False},
    {"id": 8, "text": "I reflect on my actions and think about what I could improve.", "dim": "self_awareness", "reverse": False},
    {"id": 9, "text": "I am aware of the habits or behaviors that affect my performance and relationships.", "dim": "self_awareness", "reverse": False},
    {"id": 10, "text": "I can identify situations or people that strongly affect my emotions or mood.", "dim": "self_awareness", "reverse": False},
    {"id": 11, "text": "I often copy what others do without thinking about what is right for me.", "dim": "self_awareness", "reverse": True},
    {"id": 12, "text": "I struggle to understand why I react emotionally in certain situations.", "dim": "self_awareness", "reverse": True},
    
    {"id": 13, "text": "I can make decisions on my own without always depending on others.", "dim": "decision_making", "reverse": False},
    {"id": 14, "text": "I try to think logically before making important choices.", "dim": "decision_making", "reverse": False},
    {"id": 15, "text": "I stay reasonably calm when facing unexpected problems or situations.", "dim": "decision_making", "reverse": False},
    {"id": 16, "text": "I take responsibility for the decisions I make, even when outcomes are not perfect.", "dim": "decision_making", "reverse": False},
    {"id": 17, "text": "I avoid making decisions because I fear making mistakes.", "dim": "decision_making", "reverse": True},
    {"id": 18, "text": "I often feel stuck or confused when I have to choose between options.", "dim": "decision_making", "reverse": True},
    
    {"id": 19, "text": "I can stay reasonably calm when facing stressful situations.", "dim": "emotional_balance", "reverse": False},
    {"id": 20, "text": "I recover from disappointment or failure without staying upset for too long.", "dim": "emotional_balance", "reverse": False},
    {"id": 21, "text": "I try to think clearly before reacting emotionally.", "dim": "emotional_balance", "reverse": False},
    {"id": 22, "text": "I can manage pressure from studies, responsibilities, or expectations fairly well.", "dim": "emotional_balance", "reverse": False},
    {"id": 23, "text": "My emotions often control my actions or decisions.", "dim": "emotional_balance", "reverse": True},
    {"id": 24, "text": "I struggle to stay calm when things do not go as planned.", "dim": "emotional_balance", "reverse": True},
    
    {"id": 25, "text": "I set goals for myself and try to work consistently toward them.", "dim": "drive", "reverse": False},
    {"id": 26, "text": "I stay motivated even when progress feels slow or difficult.", "dim": "drive", "reverse": False},
    {"id": 27, "text": "I take initiative instead of waiting for others to push me.", "dim": "drive", "reverse": False},
    {"id": 28, "text": "I think about how my current habits and actions can affect my future.", "dim": "drive", "reverse": False},
    {"id": 29, "text": "I often give up quickly when things become difficult or challenging.", "dim": "drive", "reverse": True},
    {"id": 30, "text": "I struggle to stay consistent with routines, habits, or goals.", "dim": "drive", "reverse": True}
]

# Complete Text Content Mapping Database
CONTENT_DB = {
    "confidence": {
        "low": {
            "label": "EMERGING", "desc": "Room for growth",
            "summary": "The student may hesitate to express ideas openly and could fear judgment in social or academic situations.",
            "good": ["Thoughtful observer", "Careful before speaking", "Good listener"],
            "improve": ["Hesitates in group settings", "Avoids attention or visibility", "Fear of embarrassment or rejection"],
            "advice": "Practice speaking in small groups and focus on small daily wins to gradually build outward confidence.",
            "next": ["Speak at least once during a class activity each day.", "Practice sharing your opinions in safe social settings first.", "Record yourself speaking for 1-2 minutes daily."]
        },
        "medium": {
            "label": "EMERGING", "desc": "Workable foundation",
            "summary": "The student shows confidence in familiar or comfortable situations but may struggle in high-pressure or unfamiliar environments.",
            "good": ["Can communicate clearly when comfortable", "Participates selectively", "Willing to express ideas in safe environments"],
            "improve": ["Inconsistent confidence", "Hesitates under pressure", "Sensitive to judgment in some situations"],
            "advice": "The student should continue using confidence positively while strengthening listening, patience, and leadership communication. Confident expression becomes more powerful when it also helps others feel heard and included.",
            "next": ["Focus on improving active listening and understanding others during conversations.", "Use your confidence to support quieter or less expressive peers in group settings.", "Practice leadership communication skills such as persuasion, storytelling, and public speaking."]
        },
        "high": {
            "label": "STANDOUT", "desc": "Clear natural strength",
            "summary": "The student is generally comfortable expressing thoughts, participating socially, and communicating confidently in different situations.",
            "good": ["Speaks confidently and expresses ideas openly.", "Comfortable in groups, discussions, and social settings.", "Takes initiative in conversations and collaborative activities."],
            "improve": ["May occasionally dominate conversations without realizing it.", "Can become overconfident in familiar or comfortable settings.", "May need to slow down and make space for quieter voices."],
            "advice": "The student should continue using confidence positively while strengthening listening, patience, and leadership communication. Confident expression becomes more powerful when it also helps others feel heard and included.",
            "next": ["Focus on improving active listening and understanding others during conversations.", "Use your confidence to support quieter or less expressive peers in group settings.", "Practice leadership communication skills such as persuasion, storytelling, and public speaking."]
        }
    },
    "self_awareness": {
        "low": {
            "label": "EMERGING", "desc": "Discovery phase",
            "summary": "The student may struggle to fully understand personal strengths, emotions, habits, and behavioral patterns.",
            "good": ["Open to learning more about themselves", "Observes others before making choices"],
            "improve": ["Difficulty identifying emotional triggers", "Easily influenced by external pressure"],
            "advice": "Developing self-awareness requires consistency and honest reflection. Small moments of tracking habits help build long-term confidence.",
            "next": ["Spend 5 minutes daily reflecting on your choices.", "Write down three personal improvement areas weekly."]
        },
        "medium": {
            "label": "EMERGING", "desc": "Strong room to grow",
            "summary": "The student shows a moderate level of self-awareness and has some understanding of personal strengths, emotions, and behavior patterns. They are capable of reflection in familiar situations but may still struggle with consistency or deeper clarity during stressful or emotional moments.",
            "good": ["Understands some personal strengths and weaknesses.", "Reflects on actions and decisions in certain situations.", "Shows growing awareness of emotions and habits."],
            "improve": ["Self-awareness may fluctuate depending on mood or environment.", "May still struggle with emotional clarity in difficult situations.", "Can occasionally rely too much on external validation or comparison."],
            "advice": "Developing stronger self-awareness requires consistency and honest reflection. Paying closer attention to habits, reactions, and emotional patterns can help you make better decisions and build stronger confidence over time.",
            "next": ["Reflect weekly on situations where you handled emotions well or poorly.", "Ask trusted people for honest feedback about your strengths and blind spots.", "Track habits or behaviors that positively or negatively affect your daily life."]
        },
        "high": {
            "label": "STANDOUT", "desc": "Excellent internal alignment",
            "summary": "The student demonstrates strong self-awareness and shows a clear understanding of personal strengths, emotions, habits, and behavioral patterns.",
            "good": ["Clearly understands personal strengths and weaknesses.", "Reflects thoughtfully on actions and decisions.", "Strong sense of identity and core values."],
            "improve": ["May occasionally overanalyze personal mistakes.", "Can become overly self-critical during setbacks."],
            "advice": "Balance high reflection with external action. Trust your instincts when executing real-world tasks.",
            "next": ["Continue journaling important structural decisions.", "Use internal self-awareness to support peer network groups."]
        }
    },
    "decision_making": {
        "low": {
            "label": "EMERGING", "desc": "Hesitant choices",
            "summary": "The student may struggle with making independent decisions and could feel overwhelmed in uncertain or high-pressure situations.",
            "good": ["Careful before making major selections.", "Open to receiving peer advice."],
            "improve": ["Overthinks simple choices", "Fears making tactical mistakes"],
            "advice": "Decision-making is a skill that improves through practice and experience. Mistakes are a natural part of learning and growth.",
            "next": ["Make minor choices independently without reassurance.", "List pros and cons explicitly on paper."]
        },
        "medium": {
            "label": "EMERGING", "desc": "Strong room to grow",
            "summary": "The student demonstrates a moderate ability to make decisions and solve problems independently. They can handle familiar situations reasonably well but may still experience hesitation, self-doubt, or overthinking during more stressful or uncertain situations.",
            "good": ["Capable of making thoughtful decisions in many situations.", "Shows willingness to take responsibility for choices.", "Can approach problems logically when emotionally balanced."],
            "improve": ["Confidence in decision-making may fluctuate under pressure.", "Sometimes delays decisions due to overthinking.", "May rely on external validation during difficult situations."],
            "advice": "Building stronger decision-making skills requires trusting yourself more consistently and becoming comfortable with uncertainty. Confidence grows through action, reflection, and experience. Focus on making clear decisions without overanalyzing every possible outcome.",
            "next": ["Set time limits for making smaller decisions to reduce overthinking.", "Practice solving problems step-by-step instead of emotionally reacting immediately.", "Challenge yourself to make decisions confidently even when outcomes are uncertain."]
        },
        "high": {
            "label": "STANDOUT", "desc": "Independent and analytical",
            "summary": "The student demonstrates strong decision-making ability and is generally capable of handling choices, uncertainty, and challenges with confidence and clarity.",
            "good": ["Makes thoughtful, standalone decisions.", "Approaches problems calmly and logically.", "Takes operational ownership of choices."],
            "improve": ["May become overly attached to personal choices.", "Frustrated when others process info slower."],
            "advice": "Continue refining your logical approach while incorporating collaborative feedback cycles from your workspace team.",
            "next": ["Practice collaborative consensus-building in team operations.", "Mentor peers on structured problem-solving steps."]
        }
    },
    "emotional_balance": {
        "low": {
            "label": "EMERGING", "desc": "Reactive patterns",
            "summary": "The student may struggle to manage emotions, stress, or pressure effectively in difficult situations.",
            "good": ["Highly empathetic and sensitive to environment.", "Cares deeply about project outcomes."],
            "improve": ["Easily overwhelmed by academic deadlines.", "Finds it difficult to bounce back from failure."],
            "advice": "Build structured cooling routines like focused respiration or intentional workspace pauses to detach from intense pressure.",
            "next": ["Utilize short mental breaks when task anxiety increases.", "Log emotional responses to review triggers later."]
        },
        "medium": {
            "label": "EMERGING", "desc": "Strong room to grow",
            "summary": "The student demonstrates a moderate level of emotional balance and can manage stress or emotional situations reasonably well in familiar environments. However, emotional control and resilience may become inconsistent during high-pressure or unexpected situations.",
            "good": ["Can manage emotions effectively in many situations.", "Shows the ability to recover from setbacks with time and support.", "Understands emotional reactions to some extent."],
            "improve": ["Emotional reactions may increase under pressure or uncertainty.", "Sometimes struggles to stay calm during frustration or disappointment.", "Emotional consistency varies depending on stress levels."],
            "advice": "Building stronger emotional balance requires learning how to pause, reflect, and respond thoughtfully during stressful moments. Developing healthy emotional habits and coping strategies can improve resilience and help you stay more balanced even during difficult situations.",
            "next": ["Identify situations that commonly trigger stress or emotional reactions.", "Practice pausing and thinking before reacting emotionally.", "Develop routines that improve emotional stability, such as sleep, exercise, or reflection."]
        },
        "high": {
            "label": "STANDOUT", "desc": "Highly resilient profile",
            "summary": "The student demonstrates strong emotional balance and is generally capable of handling stress, setbacks, and emotional situations in a calm and healthy manner.",
            "good": ["Handles structural pressure with immense calm.", "Recovers from academic failure efficiently.", "Maintains logical focus when environment changes."],
            "improve": ["May occasionally minimize emotional updates.", "Expects identical emotional management from peers."],
            "advice": "Your resilience is an asset. Ensure you remain open to acknowledging and processing emotional fatigue safely.",
            "next": ["Practice authentic communication of feelings when under extreme pressure.", "Support peers navigating stressful adjustment milestones safely."]
        }
    },
    "drive": {
        "low": {
            "label": "EMERGING", "desc": "Fluctuating focus",
            "summary": "The student may struggle with motivation, consistency, or long-term direction.",
            "good": ["Performs well when highly interested.", "Open to evaluating fresh career fields."],
            "improve": ["Loses momentum when execution gets slow.", "Avoids setting hard timeline milestones."],
            "advice": "Consistency outpaces short bursts of raw motivation. Construct atomic micro-goals to build execution discipline.",
            "next": ["Track one atomic study goal to completion every week.", "Map clear calendar timelines for key academic deliverables."]
        },
        "medium": {
            "label": "EMERGING", "desc": "Strong room to grow",
            "summary": "The student demonstrates moderate motivation and future orientation. They show interest in growth, learning, and improvement but may struggle with consistency or discipline during difficult phases. The student is capable of long-term progress but may need stronger routines, focus, and self-management to maintain momentum consistently over time.",
            "good": ["Shows interest in self-improvement and growth.", "Can stay motivated during meaningful or exciting goals.", "Demonstrates some level of discipline and responsibility."],
            "improve": ["Motivation may fluctuate depending on mood or environment.", "Sometimes struggles with consistency or long-term focus.", "Can lose momentum during setbacks or stressful periods."],
            "advice": "Long-term growth comes from consistent habits, discipline, and clarity about personal goals. Building stronger routines and learning how to stay focused during difficult periods can help improve confidence, productivity, and future success over time.",
            "next": ["Develop weekly routines that support long-term goals and consistency.", "Track progress regularly to stay motivated and accountable.", "Practice maintaining effort even during periods of low motivation."]
        },
        "high": {
            "label": "STANDOUT", "desc": "Ambitious and growth-oriented",
            "summary": "The student demonstrates strong motivation, discipline, and future orientation. They are likely to take initiative, set goals, and work consistently toward personal growth and long-term success.",
            "good": ["Highly self-motivated and structured.", "Takes operational ownership of milestones.", "Thinks systematically about long-term success."],
            "improve": ["Places high pressure on performance metrics.", "Struggles to detach and access proper rest states."],
            "advice": "Long-term success requires sustainable, balanced pacing. Protect your recovery windows to maximize ongoing output quality.",
            "next": ["Incorporate explicit rest milestones into weekly calendar configurations.", "Use strategic initiative loops to optimize team delivery pipelines."]
        }
    }
}

# =====================================================================
# 2. STATE INTERFACE CONTROLLER & CLEANERS
# =====================================================================
# Initialize persistent operational variables across screen state transitions
if "app_state" not in st.session_state:
    st.session_state.app_state = "landing"
if "student_metadata" not in st.session_state:
    st.session_state.student_metadata = {"name": "", "school": "", "class": ""}
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "current_q_idx" not in st.session_state:
    st.session_state.current_q_idx = 0
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "Overview"

def strip_emojis_from_string(text):
    emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# =====================================================================
# 3. INTERFACE SCREEN BLOCKS
# =====================================================================

# SCREEN A: THE VISUAL SYSTEM LANDING WINDOW
if st.session_state.app_state == "landing":
    st.markdown("<div style='text-align: center; margin-top: 50px;'>", unsafe_allow_html=True)
    st.title("Vidya Loop")
    st.subheader("Building India's future, one student at a time")
    st.write("Discover your unique strengths and potential through our AI-personalized assessment. Unlock insights across confidence, self-awareness, decision-making, emotional balance, and drive.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Form layout matching onboarding interface blueprints
    with st.form("metadata_onboarding_form"):
        st.subheader("Let us personalize the report.")
        st.write("These details appear in the final PDF and help the generated report feel specific to the student.")
        
        name_input = st.text_input("Student Name", placeholder="Enter your full name", value="RAM")
        school_input = st.text_input("School Name", placeholder="Enter your school name", value="High School")
        class_input = st.text_input("Class / Grade", placeholder="e.g., Class 10")
        
        col_btn_1, col_btn_2, col_btn_3 = st.columns([1, 2, 1])
        with col_btn_2:
            submit_onboarding = st.form_submit_button("Begin Assessment", use_container_width=True)
            
    if submit_onboarding:
        if name_input.strip() == "" or school_input.strip() == "":
            st.error("Please fill out your Name and School fields to initiate the dashboard analysis parameters.")
        else:
            st.session_state.student_metadata = {"name": name_input, "school": school_input, "class": class_input}
            st.session_state.app_state = "quiz"
            st.rerun()

# SCREEN B: THE SEQUENTIAL ASSESSMENT QUESTIONNAIRE
elif st.session_state.app_state == "quiz":
    total_q = len(QUESTIONS)
    current_idx = st.session_state.current_q_idx
    current_q = QUESTIONS[current_idx]
    
    # Header navigation metric blocks
    prog_pct = int((len(st.session_state.answers) / total_q) * 100)
    
    col_q1, col_q2 = st.columns([3, 1])
    with col_q1:
        st.caption(f"Question {current_idx + 1} of {total_q} | {len(st.session_state.answers)} attempted")
        st.progress(prog_pct / 100.0)
    with col_q2:
        # Determine the user-facing title of the active dimension
        dim_titles = {
            "confidence": "Confidence & Expression", "self_awareness": "Self-Awareness",
            "decision_making": "Decision-Making Style", "emotional_balance": "Emotional Balance",
            "drive": "Drive & Future Orientation"
        }
        st.metric(label="Current Dimension", value=dim_titles[current_q["dim"]])
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Main Question Layout Card
    st.info(current_q["text"])
    
    # Set up selected default tracking index values
    saved_ans = st.session_state.answers.get(current_q["id"], None)
    default_sel_idx = 2 if saved_ans is None else (saved_ans - 1 if not current_q["reverse"] else 5 - saved_ans)
    
    choice_map = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]
    selected_option = st.radio("Select your response option:", choice_map, index=default_sel_idx)
    
    # Convert chosen string value back to standard numerical integer weights
    raw_numerical_val = choice_map.index(selected_option) + 1
    final_assigned_weight = raw_numerical_val if not current_q["reverse"] else (6 - raw_numerical_val)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Stepper Control Actions
    col_nav_1, col_nav_2, col_nav_3 = st.columns([1, 4, 1])
    with col_nav_1:
        if current_idx > 0:
            if st.button("Previous", use_container_width=True):
                st.session_state.answers[current_q["id"]] = final_assigned_weight
                st.session_state.current_q_idx -= 1
                st.rerun()
    with col_nav_3:
        if current_idx < total_q - 1:
            if st.button("Next", use_container_width=True):
                st.session_state.answers[current_q["id"]] = final_assigned_weight
                st.session_state.current_q_idx += 1
                st.rerun()
        else:
            if st.button("Submit", type="primary", use_container_width=True):
                st.session_state.answers[current_q["id"]] = final_assigned_weight
                st.session_state.app_state = "dashboard"
                st.rerun()

# SCREEN C: THE DYNAMIC MULTI-PAGE STYLED ASSESSMENTS REPORT DASHBOARD
elif st.session_state.app_state == "dashboard":
    
    # Compute aggregate operational scores from user inputs
    aggregated_scores = {"confidence": 0, "self_awareness": 0, "decision_making": 0, "emotional_balance": 0, "drive": 0}
    for q in QUESTIONS:
        aggregated_scores[q["dim"]] += st.session_state.answers.get(q["id"], 3) # Fallback baseline default score to Neutral
        
    # Calculate global tracking parameters for priority routing
    sorted_dimensions = sorted(aggregated_scores.items(), key=lambda kv: kv[1])
    lowest_dimension_key = sorted_dimensions[0][0]
    highest_dimension_key = sorted_dimensions[-1][0]
    
    meta = st.session_state.student_metadata
    
    # Top Level Premium Application Branding Header Card
    st.markdown(
        f"""
        <div style="background-color: #114B43; color: white; padding: 25px; border-radius: 12px; margin-bottom: 20px;">
            <span style="background-color: rgba(255,255,255,0.2); padding: 5px 12px; border-radius: 20px; font-size: 0.85em; font-weight: bold;">PERSONALIZED GROWTH REPORT</span>
            <h1 style="color: white; margin: 10px 0 5px 0; font-size: 2.2em;">Vidyaloop Personality Report</h1>
            <p style="margin: 0; opacity: 0.9; font-size: 1.05em;">
                👤 <b>Name:</b> {meta['name']} &nbsp;|&nbsp; 🏫 <b>School:</b> {meta['school']} &nbsp;|&nbsp; 🎓 <b>Class/Grade:</b> {meta['class'] if meta['class'] else 'N/A'}
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Interactive Tab Navigation matching multi-page interface configurations
    navigation_tabs_list = ["Overview", "Confidence & Expression", "Self-Awareness", "Decision-Making Style", "Emotional Balance", "Drive & Future Orientation", "Personality Snapshot"]
    chosen_tab = st.radio("Navigate Report Pages:", navigation_tabs_list, horizontal=True, label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # PAGE 1 BLOCK: OVERVIEW TAB ENGINE
    if chosen_tab == "Overview":
        st.subheader("Core Dimensions Growth Matrix")
        st.write("Review your scoring evaluations across the five developmental tracking profiles.")
        
        # Grid block containers mapping scores visually with matching badges
        grid_cols = st.columns(5)
        dimension_map_indices = [
            ("confidence", "CONFIDENCE & EXPRESSION", "confidence"),
            ("self_awareness", "SELF-AWARENESS", "self_awareness"),
            ("decision_making", "DECISION-MAKING STYLE", "decision_making"),
            ("emotional_balance", "EMOTIONAL BALANCE", "emotional_balance"),
            ("drive", "DRIVE & FUTURE ORIENTATION", "drive")
        ]
        
        for idx, (key, display_title, db_ref) in enumerate(dimension_map_indices):
            raw_val = aggregated_scores[key]
            tier_evaluated = get_tier(key, raw_val)
            content_snippet = CONTENT_DB[db_ref][tier_evaluated]
            
            # Badge styles matching production color profiles
            badge_color = "#EBF5FF" if content_snippet['label'] == "STANDOUT" else "#F3F4F6"
            text_color = "#1E429F" if content_snippet['label'] == "STANDOUT" else "#4B5563"
            
            with grid_cols[idx]:
                st.markdown(
                    f"""
                    <div style="background-color: white; border: 1px solid #E5E7EB; border-radius: 12px; padding: 20px; text-align: center; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
                        <p style="font-size: 0.8em; color: #6B7280; font-weight: bold; margin-bottom: 10px; height: 35px; overflow: hidden;">{display_title}</p>
                        <h2 style="margin: 5px 0; color: #111827; font-size: 2.1em;">{raw_val}<span style="font-size: 0.5em; color: #9CA3AF;">/30</span></h2>
                        <div style="margin-top: 10px; margin-bottom: 5px;">
                            <span style="background-color: {badge_color}; color: {text_color}; padding: 4px 12px; border-radius: 12px; font-size: 0.75em; font-weight: bold;">{content_snippet['label']}</span>
                        </div>
                        <p style="font-size: 0.75em; color: #9CA3AF; margin: 0;">{content_snippet['desc']}</p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Unified Overall Analysis Card Module
        st.subheader("Overall Analysis")
        analysis_summary_paragraph = (
            f"Based on your configuration profile inputs, your responses demonstrate a balanced ecosystem. "
            f"Your strongest foundational execution space maps directly to your high performance score in "
            f"<b>{dim_titles[highest_dimension_key]}</b>, which acts as a core behavioral driver. "
            f"Concurrently, your primary strategic milestone optimization pathway lies within expanding your habits "
            f"inside <b>{dim_titles[lowest_dimension_key]}</b>. By addressing this space first, you will establish a powerful cascading "
            f"positive impact across your remaining behavioral traits."
        )
        st.info(analysis_summary_paragraph)
        
    # PAGES 2 TO 6 BLOCKS: INDIVIDUAL TRAIT PAGES
    elif chosen_tab in dim_titles.values():
        # Find internal tracking keys from inverted mapping setups
        inverse_title_lookup = {v: k for k, v in dim_titles.items()}
        selected_key = inverse_title_lookup[chosen_tab]
        
        score_metric = aggregated_scores[selected_key]
        tier_evaluated = get_tier(selected_key, score_metric)
        text_payload = CONTENT_DB[selected_key][tier_evaluated]
        
        # Display trait page metadata block headers
        col_page_1, col_page_2 = st.columns([3, 1])
        with col_page_1:
            st.subheader(f"{chosen_tab} Analysis")
            st.caption(text_payload["desc"])
        with col_page_2:
            st.metric(label="Dimension Raw Score", value=f"{score_metric} / 30")
            st.progress(score_metric / 30.0)
            
        st.markdown("<br>", unsafe_allow_html=True)
        st.write(text_payload["summary"])
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Layout arrangement matching the separate container boxes from the screenshots
        col_box_1, col_box_2 = st.columns(2)
        with col_box_1:
            st.markdown("<div style='background-color: #EEFBF7; padding: 20px; border-radius: 8px; border-left: 5px solid #22C55E; height: 100%;'>", unsafe_allow_html=True)
            st.markdown("<b style='color: #166534;'>🟢 Strengths</b>", unsafe_allow_html=True)
            for point in text_payload["good"]:
                st.markdown(f"<p style='color: #1E3A1E; margin: 8px 0;'>• {point}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col_box_2:
            st.markdown("<div style='background-color: #FFF7ED; padding: 20px; border-radius: 8px; border-left: 5px solid #F97316; height: 100%;'>", unsafe_allow_html=True)
            st.markdown("<b style='color: #9A3412;'>⚠️ Growth Areas</b>", unsafe_allow_html=True)
            for point in text_payload["improve"]:
                st.markdown(f"<p style='color: #431407; margin: 8px 0;'>• {point}</p>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Improvement & Stepper Guidance Sections
        st.subheader("Improvement Advice")
        st.write(text_payload["advice"])
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Action Steps")
        for i, step in enumerate(text_payload["next"]):
            st.markdown(
                f"""
                <div style="background-color: white; border: 1px solid #E5E7EB; padding: 15px; border-radius: 8px; margin-bottom: 10px; display: flex; align-items: center;">
                    <div style="background-color: #EBF5FF; color: #1E429F; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-right: 15px;">
                        {i+1}
                    </div>
                    <div style="color: #374151; font-size: 0.95em;">{step}</div>
                </div>
                """, 
                unsafe_allow_html=True
            )

    # PAGE 7 BLOCK: DESIGNATED DARK-THEMED SNAPSHOT PAGE AT SYSTEM END
    elif chosen_tab == "Personality Snapshot":
        st.markdown(
            f"""
            <div style="background-color: #201A1A; color: #F9F6F6; padding: 35px; border-radius: 16px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);">
                <h2 style="color: #F9F6F6; margin-top: 0;">Overall Personality Snapshot</h2>
                <p style="font-size: 0.85em; opacity: 0.7; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 20px;">
                    Strongest areas, growth areas, focus areas, and final encouragement.
                </p>
                <p style="font-size: 1.1em; line-height: 1.6; opacity: 0.95; margin-bottom: 30px;">
                    Your profile maps a structured equilibrium between your active tracking configurations. When you deliberately harness your 
                    deep internal self-reflection capabilities into clear execution vectors, you effectively construct an automated path 
                    toward transforming high-level personal plans into concrete, real-world execution across your peer networks.
                </p>
                
                <div style="display: flex; gap: 20px; margin-bottom: 30px;">
                    <div style="background-color: rgba(255,255,255,0.04); padding: 20px; border-radius: 12px; flex: 1; border: 1px solid rgba(255,255,255,0.08);">
                        <b style="color: #86EFAC; font-size: 0.9em; text-transform: uppercase;">• Strongest Areas</b>
                        <p style="font-size: 1.2em; font-weight: bold; margin: 10px 0 0 0; color: #F9F6F6;">{dim_titles[highest_dimension_key]}</p>
                    </div>
                    <div style="background-color: rgba(255,255,255,0.04); padding: 20px; border-radius: 12px; flex: 1; border: 1px solid rgba(255,255,255,0.08);">
                        <b style="color: #FDBA74; font-size: 0.9em; text-transform: uppercase;">• Growth Areas</b>
                        <p style="font-size: 1.2em; font-weight: bold; margin: 10px 0 0 0; color: #F9F6F6;">{dim_titles[lowest_dimension_key]}</p>
                    </div>
                </div>
                
                <h4 style="color: #F9F6F6; margin-bottom: 15px;">Recommended Action Focus Path</h4>
                <div style="display: flex; gap: 15px; margin-bottom: 40px;">
                    <div style="background-color: #2D2424; padding: 20px; border-radius: 8px; flex: 1; border-top: 4px solid #FDBA74;">
                        <span style="font-size: 0.75em; opacity: 0.6; font-weight: bold; display: block; margin-bottom: 5px;">FOCUS 01</span>
                        <p style="font-size: 0.9em; margin: 0; opacity: 0.9;">Practice one structured action habit selection loop daily to build momentum under pressure.</p>
                    </div>
                    <div style="background-color: #2D2424; padding: 20px; border-radius: 8px; flex: 1; border-top: 4px solid #A7F3D0;">
                        <span style="font-size: 0.75em; opacity: 0.6; font-weight: bold; display: block; margin-bottom: 5px;">FOCUS 02</span>
                        <p style="font-size: 0.9em; margin: 0; opacity: 0.9;">Channel natural communication assets to balance collaborative milestones with group peers.</p>
                    </div>
                    <div style="background-color: #2D2424; padding: 20px; border-radius: 8px; flex: 1; border-top: 4px solid #6366F1;">
                        <span style="font-size: 0.75em; opacity: 0.6; font-weight: bold; display: block; margin-bottom: 5px;">FOCUS 03</span>
                        <p style="font-size: 0.9em; margin: 0; opacity: 0.9;">Review tracking metrics weekly to adapt goal systems without creating performance fatigue.</p>
                    </div>
                </div>
                
                <div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 25px;">
                    <b style="color: #F9F6F6; font-size: 0.95em; text-transform: uppercase; letter-spacing: 0.5px; display: block; margin-bottom: 8px;">Final Encouragement Note</b>
                    <p style="font-size: 0.95em; line-height: 1.5; opacity: 0.8; margin: 0;">
                        This report is an architectural growth guide, not a fixed classification label. Your calculated baseline strengths confirm 
                        that you already possess the capabilities needed to scale your framework. Keep iterating execution choices consistently, 
                        trust your reflective processing logic, and celebrate your ongoing transformation progress milestones.
                    </p>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Global Action Trigger Buttons matching user flow layout
        col_f1, col_f2, col_f3 = st.columns([2, 1, 1])
        with col_f2:
            # Generate automated text report asset payload for extraction utilities
            string_report_buffer = []
            for d_title, d_key in inverse_title_lookup.items():
                t_score = aggregated_scores[d_key]
                t_tier = get_tier(d_key, t_score)
                string_report_buffer.append(f"--- {d_title.upper()} ({t_score}/30) ---\n" + CONTENT_DB[d_key][t_tier]["summary"])
            
            st.download_button(
                label="📥 Download Professional PDF/Text",
                data=strip_emojis_from_string("\n\n".join(string_report_buffer)),
                file_name=f"{meta['name']}_Personality_Report.txt",
                use_container_width=True
            )
        with col_f3:
            if st.button("🔄 Take Assessment Again", use_container_width=True):
                st.session_state.app_state = "landing"
                st.session_state.answers = {}
                st.session_state.current_q_idx = 0
                st.rerun()