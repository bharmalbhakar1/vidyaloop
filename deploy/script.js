// 1. DATA DICTIONARIES AND VERBATIM SNIPPETS (From PDA framework.docx)
const DATA_BOUNDARIES = {
    "confidence": { low: [5, 11], medium: [12, 18], high: [19, 30] },
    "self_awareness": { low: [6, 13], medium: [14, 22], high: [23, 30] },
    "decision_making": { low: [6, 13], medium: [14, 22], high: [23, 30] },
    "emotional_balance": { low: [6, 13], medium: [14, 22], high: [23, 30] },
    "drive": { low: [6, 13], medium: [14, 22], high: [23, 30] }
};

const MAIN_SNIPPETS = {
    "confidence": {
        "low": {
            label: "EMERGING", desc: "Room for growth",
            summary: "The student may hesitate to express ideas openly and could fear judgment in social or academic situations.",
            good: ["Thoughtful observer", "Careful before speaking", "Good listener"],
            improve: ["Hesitates in group settings", "Avoids attention or visibility", "Fear of embarrassment or rejection"],
            advice: "Practice speaking in small groups and focus on progress, not perfection.",
            next: ["Speak at least once during a class, discussion, or group activity each day.", "Practice sharing your opinions in smaller or safer social settings first.", "Record yourself speaking for 1-2 minutes daily to become more comfortable."]
        },
        "medium": {
            label: "EMERGING", desc: "Workable foundation",
            summary: "The student shows confidence in familiar or comfortable situations but may struggle in high-pressure or unfamiliar environments.",
            good: ["Can communicate clearly when comfortable", "Participates selectively", "Willing to express ideas in safe environments"],
            improve: ["Inconsistent confidence", "Hesitates under pressure", "Sensitive to judgment in some situations"],
            advice: "Practice public communication regularly, participate more actively in discussions, and take small social risks consistently.",
            next: ["Participate more actively in group discussions or collaborative activities.", "Challenge yourself to speak in situations that feel slightly uncomfortable or unfamiliar.", "Practice organizing your thoughts before speaking to improve confidence under pressure."]
        },
        "high": {
            label: "STANDOUT", desc: "Clear natural strength",
            summary: "The student is generally comfortable expressing thoughts, participating socially, and communicating confidently in different situations.",
            good: ["Speaks confidently", "Comfortable in groups", "Takes initiative in conversations", "Expresses ideas openly"],
            improve: ["May occasionally dominate conversations", "Can become overconfident in familiar settings"],
            advice: "The student should continue using confidence positively while strengthening listening, patience, and leadership communication. Confident expression becomes more powerful when it also helps others feel heard and included.",
            next: ["Focus on improving active listening and understanding others during conversations.", "Use your confidence to support quieter or less expressive peers in group settings.", "Practice leadership communication skills such as persuasion, storytelling, and public speaking."]
        }
    },
    "self_awareness": {
        "low": {
            label: "EMERGING", desc: "Discovery phase",
            summary: "The student may struggle to fully understand personal strengths, emotions, habits, and behavioral patterns. They may react impulsively in certain situations or depend heavily on external opinions and validation.",
            good: ["Open to learning more about themselves and their personal growth.", "May observe others carefully before making decisions.", "Shows potential for growth through reflection."],
            improve: ["Difficulty identifying emotional triggers or behavioral patterns.", "Can be easily influenced by peers or external pressure.", "Limited clarity about strengths or personal direction."],
            advice: "Self-awareness develops gradually through observation, reflection, and honest thinking.",
            next: ["Spend 5 minutes daily reflecting on your actions, emotions, or decisions.", "Write down three strengths and three improvement areas about yourself.", "Notice situations that affect your mood, confidence, or reactions."]
        },
        "medium": {
            label: "EMERGING", desc: "Strong room to grow",
            summary: "The student shows a moderate level of self-awareness and has some understanding of personal strengths, emotions, and behavior patterns. They are capable of reflection in familiar situations but may still struggle with consistency during stressful moments.",
            good: ["Understands some personal strengths and weaknesses.", "Reflects on actions and decisions in certain situations.", "Shows growing awareness of emotions and habits."],
            improve: ["Self-awareness may fluctuate depending on mood or environment.", "May still struggle with emotional clarity in difficult situations.", "Can occasionally rely too much on external validation or comparison."],
            advice: "Developing stronger self-awareness requires consistency and honest reflection. Paying closer attention to your habits, reactions, and emotional patterns can help you make better decisions.",
            next: ["Reflect weekly on situations where you handled emotions well or poorly.", "Ask trusted people for honest feedback about your strengths and blind spots.", "Track habits or behaviors that positively or negatively affect your daily life."]
        },
        "high": {
            label: "STANDOUT", desc: "Excellent internal alignment",
            summary: "The student demonstrates strong self-awareness and shows a clear understanding of personal strengths, emotions, habits, and behavioral patterns. They are capable of reflecting on their actions and learning from experiences.",
            good: ["Clearly understands personal strengths and improvement areas.", "Reflects thoughtfully on actions, emotions, and decisions.", "Shows emotional understanding and personal clarity."],
            improve: ["May occasionally overanalyze situations or personal mistakes.", "Can become overly self-critical during setbacks or failures.", "May place high expectations on personal growth."],
            advice: "Strong self-awareness is a powerful foundation for growth and leadership. The next step is learning how to balance reflection with action and confidence.",
            next: ["Continue journaling or reflecting on important experiences and decisions.", "Use self-awareness to improve communication and relationships with others.", "Focus on balancing reflection with confident action and experimentation."]
        }
    },
    "decision_making": {
        "low": {
            label: "EMERGING", desc: "Hesitant choices",
            summary: "The student may struggle with making independent decisions and could feel overwhelmed in uncertain or high-pressure situations. They may frequently overthink choices or rely heavily on others for guidance.",
            good: ["Careful before making important choices.", "Open to seeking advice and considering different perspectives.", "Shows potential to become more confident with practice."],
            improve: ["Overthinks decisions and fears making mistakes.", "May avoid responsibility or delay important choices.", "Can feel confused or anxious during uncertain situations."],
            advice: "Decision-making is a skill that improves through practice and experience. Mistakes are a natural part of learning and growth.",
            next: ["Start making small daily decisions independently without asking for reassurance.", "Practice listing pros and cons before making important choices.", "Reflect on past decisions and identify lessons instead of focusing only on mistakes."]
        },
        "medium": {
            label: "EMERGING", desc: "Strong room to grow",
            summary: "The student demonstrates a moderate ability to make decisions and solve problems independently. They can handle familiar situations reasonably well but may still experience hesitation during more stressful or uncertain situations.",
            good: ["Capable of making thoughtful decisions in many situations.", "Shows willingness to take responsibility for choices.", "Can approach problems logically when emotionally balanced."],
            improve: ["Confidence in decision-making may fluctuate under pressure.", "Sometimes delays decisions due to overthinking.", "May rely on external validation during difficult situations."],
            advice: "Building stronger decision-making skills requires trusting yourself more consistently and becoming comfortable with uncertainty. Focus on making clear decisions without overanalyzing every outcome.",
            next: ["Set time limits for making smaller decisions to reduce overthinking.", "Practice solving problems step-by-step instead of emotionally reacting immediately.", "Challenge yourself to make decisions confidently even when outcomes are uncertain."]
        },
        "high": {
            label: "STANDOUT", desc: "Independent and analytical",
            summary: "The student demonstrates strong decision-making ability and is generally capable of handling choices, uncertainty, and challenges with confidence and clarity. They are likely to think logically.",
            good: ["Makes independent and thoughtful decisions.", "Handles challenges and uncertainty with confidence.", "Takes responsibility for actions and outcomes.", "Approaches problems logically and calmly."],
            improve: ["May occasionally become overly confident in personal judgment.", "Can take on too much responsibility during group situations.", "May feel frustrated when others struggle to make decisions quickly."],
            advice: "Strong decision-making is a valuable life skill. The next stage of growth involves balancing confidence with flexibility, collaboration, and emotional awareness.",
            next: ["Practice collaborative decision-making during group activities or projects.", "Continue improving problem-solving skills through real-world challenges.", "Focus on balancing confidence with patience, flexibility, and active listening."]
        }
    },
    "emotional_balance": {
        "low": {
            label: "EMERGING", desc: "Reactive patterns",
            summary: "The student may struggle to manage emotions, stress, or pressure effectively in difficult situations. Emotional reactions may sometimes affect decision-making, confidence, or relationships.",
            good: ["Emotionally sensitive and aware of personal feelings.", "Cares deeply about outcomes and relationships.", "Has the potential to build resilience through reflection."],
            improve: ["Gets emotionally overwhelmed during stressful situations.", "May react impulsively under pressure or frustration.", "Finds it difficult to recover quickly from setbacks or criticism."],
            advice: "Emotional balance is a skill that develops gradually through awareness, reflection, and healthy coping habits.",
            next: ["Practice calming techniques such as deep breathing or short breaks during stressful moments.", "Reflect on emotional situations before reacting or responding immediately.", "Build healthy routines such as exercise, journaling, or mindfulness to manage stress better."]
        },
        "medium": {
            label: "EMERGING", desc: "Strong room to grow",
            summary: "The student demonstrates a moderate level of emotional balance and can manage stress reasonably well in familiar environments. However, emotional control and resilience may become inconsistent during high-pressure situations.",
            good: ["Can manage emotions effectively in many situations.", "Shows the ability to recover from setbacks with time and support.", "Understands emotional reactions to some extent."],
            improve: ["Emotional reactions may increase under pressure or uncertainty.", "Sometimes struggles to stay calm during frustration or disappointment.", "Emotional consistency varies depending on stress levels."],
            advice: "Building stronger emotional balance requires learning how to pause, reflect, and respond thoughtfully during stressful moments. Developing healthy coping strategies can improve resilience.",
            next: ["Identify situations that commonly trigger stress or emotional reactions.", "Practice pausing and thinking before reacting emotionally.", "Develop routines that improve emotional stability, such as sleep, exercise, or reflection."]
        },
        "high": {
            label: "STANDOUT", desc: "Highly resilient profile",
            summary: "The student demonstrates strong emotional balance and is generally capable of handling stress, setbacks, and emotional situations in a calm and healthy manner. They are likely to recover from challenges effectively.",
            good: ["Handles pressure and setbacks calmly.", "Shows emotional resilience and self-control.", "Thinks clearly during stressful situations.", "Maintains emotional stability in challenging environments."],
            improve: ["May occasionally suppress emotions instead of expressing them openly.", "Can take on emotional burdens without seeking support.", "May expect the same emotional control from others."],
            advice: "Strong emotional balance is an important strength that supports growth, leadership, and healthy relationships. Continue developing emotional awareness.",
            next: ["Continue practicing healthy stress-management habits and emotional reflection.", "Support others emotionally while maintaining personal boundaries.", "Focus on balancing emotional control with honest emotional expression."]
        }
    },
    "drive": {
        "low": {
            label: "EMERGING", desc: "Fluctuating focus",
            summary: "The student may struggle with motivation, consistency, or long-term direction. They may find it difficult to stay disciplined, take initiative, or remain focused on goals over time.",
            good: ["Has potential for growth when properly motivated or guided.", "May perform well when emotionally engaged or interested.", "Open to discovering personal interests and future goals."],
            improve: ["Struggles with consistency and long-term focus.", "Can lose motivation easily during difficult situations.", "May avoid initiative or responsibility without external pressure."],
            advice: "Motivation and discipline develop through habits, routines, and repeated action. Small consistent efforts often create bigger long-term results.",
            next: ["Set one small achievable goal each week and track your progress.", "Create simple daily routines for studies, health, or skill-building.", "Break large goals into smaller tasks to avoid feeling overwhelmed."]
        },
        "medium": {
            label: "EMERGING", desc: "Strong room to grow",
            summary: "The student demonstrates moderate motivation and future orientation. They show interest in growth, learning, and improvement but may struggle with consistency or discipline during difficult phases.",
            good: ["Shows interest in self-improvement and growth.", "Can stay motivated during meaningful or exciting goals.", "Demonstrates some level of discipline and responsibility."],
            improve: ["Motivation may fluctuate depending on mood or environment.", "Sometimes struggles with consistency or long-term focus.", "Can lose momentum during setbacks or stressful periods."],
            advice: "Long-term growth comes from consistent habits, discipline, and clarity about personal goals. Building stronger routines can help improve confidence.",
            next: ["Develop weekly routines that support long-term goals and consistency.", "Track progress regularly to stay motivated and accountable.", "Practice maintaining effort even during periods of low motivation."]
        },
        "high": {
            label: "STANDOUT", desc: "Ambitious and growth-oriented",
            summary: "The student demonstrates strong motivation, discipline, and future orientation. They are likely to take initiative, set goals, and work consistently toward personal growth and long-term success.",
            good: ["Highly motivated and growth-oriented.", "Takes initiative and responsibility independently.", "Shows strong discipline and consistency.", "Thinks long-term and plans for future success."],
            improve: ["May place excessive pressure on personal performance or achievement.", "Can become frustrated when progress feels slow.", "May struggle to relax or balance productivity with recovery."],
            advice: "Strong drive and ambition are valuable strengths, but long-term success also requires balance, patience, and adaptability. Protect your recovery windows.",
            next: ["Continue setting meaningful long-term goals while balancing rest and recovery.", "Focus on sustainable habits instead of perfection or constant productivity.", "Use your motivation and initiative to inspire or support others positively."]
        }
    }
};

const ASSESSMENT_PROMPTS = [
    { id: 1, text: "I speak up in class or group discussions even when I am not fully sure of my answer.", dim: "confidence", reverse: false },
    { id: 2, text: "I feel comfortable sharing my opinions with others.", dim: "confidence", reverse: false },
    { id: 3, text: "I can start or continue conversations without feeling too nervous.", dim: "confidence", reverse: false },
    { id: 4, text: "I participate actively when working in teams or groups.", dim: "confidence", reverse: false },
    { id: 5, text: "I avoid speaking in front of others because I fear being judged.", dim: "confidence", reverse: true },
    { id: 6, text: "I often stay quiet even when I have something important to say.", dim: "confidence", reverse: true },
    { id: 7, text: "I understand what my strengths are in studies, activities, or daily life.", dim: "self_awareness", reverse: false },
    { id: 8, text: "I reflect on my actions and think about what I could improve.", dim: "self_awareness", reverse: false },
    { id: 9, text: "I am aware of the habits or behaviors that affect my performance and relationships.", dim: "self_awareness", reverse: false },
    { id: 10, text: "I can identify situations or people that strongly affect my emotions or mood.", dim: "self_awareness", reverse: false },
    { id: 11, text: "I often copy what others do without thinking about what is right for me.", dim: "self_awareness", reverse: true },
    { id: 12, text: "I struggle to understand why I react emotionally in certain situations.", dim: "self_awareness", reverse: true },
    { id: 13, text: "I can make decisions on my own without always depending on others.", dim: "decision_making", reverse: false },
    { id: 14, text: "I try to think logically before making important choices.", dim: "decision_making", reverse: false },
    { id: 15, text: "I stay reasonably calm when facing unexpected problems or situations.", dim: "decision_making", reverse: false },
    { id: 16, text: "I take responsibility for the decisions I make, even when outcomes are not perfect.", dim: "decision_making", reverse: false },
    { id: 17, text: "I avoid making decisions because I fear making mistakes.", dim: "decision_making", reverse: true },
    { id: 18, text: "I often feel stuck or confused when I have to choose between options.", dim: "decision_making", reverse: true },
    { id: 19, text: "I can stay reasonably calm when facing stressful situations.", dim: "emotional_balance", reverse: false },
    { id: 20, text: "I recover from disappointment or failure without staying upset for too long.", dim: "emotional_balance", reverse: false },
    { id: 21, text: "I try to think clearly before reacting emotionally.", dim: "emotional_balance", reverse: false },
    { id: 22, text: "I can manage pressure from studies, responsibilities, or expectations fairly well.", dim: "emotional_balance", reverse: false },
    { id: 23, text: "My emotions often control my actions or decisions.", dim: "emotional_balance", reverse: true },
    { id: 24, text: "I struggle to stay calm when things do not go as planned.", dim: "emotional_balance", reverse: true },
    { id: 25, text: "I set goals for myself and try to work consistently toward them.", dim: "drive", reverse: false },
    { id: 26, text: "I stay motivated even when progress feels slow or difficult.", dim: "drive", reverse: false },
    { id: 27, text: "I take initiative instead of waiting for others to push me.", dim: "drive", reverse: false },
    { id: 28, text: "I think about how my current habits and actions can affect my future.", dim: "drive", reverse: false },
    { id: 29, text: "I often give up quickly when things become difficult or challenging.", dim: "drive", reverse: true },
    { id: 30, text: "I struggle to stay consistent with routines, habits, or goals.", dim: "drive", reverse: true }
];

// 2. STATE PIPELINE SYSTEM CONTROLLERS
let currentQuestionIndex = 0;
let userResponses = {};
let studentData = { name: "", school: "", grade: "" };

const dimTitles = {
    "confidence": "Confidence & Expression", "self_awareness": "Self-Awareness",
    "decision_making": "Decision-Making Style", "emotional_balance": "Emotional Balance",
    "drive": "Drive & Future Orientation"
};

function determineTier(dimension, score) {
    const limits = DATA_BOUNDARIES[dimension];
    if (score >= limits.low[0] && score <= limits.low[1]) return "low";
    if (score >= limits.medium[0] && score <= limits.medium[1]) return "medium";
    return "high";
}

// 3. UI VIEW TRANSITION ROUTINES
function startAssessment() {
    const nameVal = document.getElementById("student-name").value.trim();
    const schoolVal = document.getElementById("school-name").value.trim();
    const gradeVal = document.getElementById("class-grade").value.trim();

    if (!nameVal || !schoolVal) {
        alert("Please complete Name and School profile metrics before launching the execution matrix.");
        return;
    }

    studentData = { name: nameVal, school: schoolVal, grade: gradeVal || "N/A" };
    
    // Transition views
    document.getElementById("onboarding-screen").classList.remove("active");
    document.getElementById("quiz-screen").classList.add("active");
    
    renderCurrentQuestion();
}

function renderCurrentQuestion() {
    const prompt = ASSESSMENT_PROMPTS[currentQuestionIndex];
    const totalQuestions = ASSESSMENT_PROMPTS.length;

    // Track active headers
    document.getElementById("quiz-meta").innerText = `Question ${currentQuestionIndex + 1} of ${totalQuestions} | ${Object.keys(userResponses).length} attempted`;
    
    const pct = ((currentQuestionIndex) / totalQuestions) * 100;
    document.getElementById("quiz-progress-bar").style.width = `${pct}%`;
    document.getElementById("current-dimension-name").innerText = dimTitles[prompt.dim];
    
    // Card info
    document.getElementById("card-dimension-tag").innerText = dimTitles[prompt.dim].toUpperCase();
    document.getElementById("question-text").innerText = prompt.text;

    // Restore saved selections or fallback to standard Neutral option
    const previouslySavedWeight = userResponses[prompt.id];
    const radioInputs = document.getElementsByName("response");
    
    let defaultRadioIndexValue = 2; // Neutral index mapping
    if (previouslySavedWeight !== undefined) {
        // Reverse resolve if the prompt was standard or reverse scored
        let rawScoreWeightValue = previouslySavedWeight;
        if (prompt.reverse) {
            rawScoreWeightValue = 6 - previouslySavedWeight;
        }
        defaultRadioIndexValue = rawScoreWeightValue - 1;
    }

    for (let i = 0; i < radioInputs.length; i++) {
        radioInputs[i].checked = (i === defaultRadioIndexValue);
    }

    // Nav control updates
    document.getElementById("prev-btn").disabled = (currentQuestionIndex === 0);
    document.getElementById("next-btn").innerText = (currentQuestionIndex === totalQuestions - 1) ? "Submit Report" : "Next →";
}

function saveActiveResponse() {
    const prompt = ASSESSMENT_PROMPTS[currentQuestionIndex];
    const radioInputs = document.getElementsByName("response");
    let chosenRawValue = 3; 

    for (let i = 0; i < radioInputs.length; i++) {
        if (radioInputs[i].checked) {
            chosenRawValue = parseInt(radioInputs[i].value);
            break;
        }
    }

    // Process reverse-scoring calculation configurations safely
    const calculationWeightValue = prompt.reverse ? (6 - chosenRawValue) : chosenRawValue;
    userResponses[prompt.id] = calculationWeightValue;
}

function goToNextQuestion() {
    saveActiveResponse();
    if (currentQuestionIndex < ASSESSMENT_PROMPTS.length - 1) {
        currentQuestionIndex++;
        renderCurrentQuestion();
    } else {
        compileAndDisplayReportDashboard();
    }
}

function goToPrevQuestion() {
    saveActiveResponse();
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        renderCurrentQuestion();
    }
}

// 4. DYNAMIC SYNTHESIS GENERATION CORE PIPELINE
function compileAndDisplayReportDashboard() {
    // 1. Calculate Dimension Raw Aggregate Metrics
    let scores = { confidence: 0, self_awareness: 0, decision_making: 0, emotional_balance: 0, drive: 0 };
    ASSESSMENT_PROMPTS.forEach(q => {
        scores[q.dim] += (userResponses[q.id] || 3);
    });

    // 2. Identify Peak Bounds for Cross-Trend Intelligence Synthetics
    let items = Object.keys(scores).map(k => [k, scores[k]]);
    items.sort((a, b) => a[1] - b[1]);
    let lowestKey = items[0][0];
    let highestKey = items[items.length - 1][0];

    // Mount header data profiles securely
    document.getElementById("out-name").innerText = studentData.name;
    document.getElementById("out-school").innerText = studentData.school;
    document.getElementById("out-grade").innerText = studentData.grade;

    // 3. Build Matrix Card Layout Nodes dynamically
    const dimRefs = [
        { key: "confidence", id: "card-m-conf", title: "CONFIDENCE & EXPRESSION" },
        { key: "self_awareness", id: "card-m-aware", title: "SELF-AWARENESS" },
        { key: "decision_making", id: "card-m-dec", title: "DECISION-MAKING STYLE" },
        { key: "emotional_balance", id: "card-m-bal", title: "EMOTIONAL BALANCE" },
        { key: "drive", id: "card-m-drive", title: "DRIVE & FUTURE ORIENTATION" }
    ];

    dimRefs.forEach(d => {
        const rawScore = scores[d.key];
        const tier = determineTier(d.key, rawScore);
        const chunk = MAIN_SNIPPETS[d.key][tier];
        const badgeClass = chunk.label === "STANDOUT" ? "status-standout" : "status-emerging";

        document.getElementById(d.id).innerHTML = `
            <p>${d.title}</p>
            <h2>${rawScore}<span class="small-text">/30</span></h2>
            <div><span class="badge-status ${badgeClass}">${chunk.label}</span></div>
            <p style="font-size:0.75em; color:#9CA3AF; margin-top:5px; height:auto;">${chunk.desc}</p>
        `;

        // 4. Mount Custom Individual Tab Profiles Dynamic HTML Loops
        let goodListItems = chunk.good.map(i => `<li>${i}</li>`).join("");
        let improveListItems = chunk.improve.map(i => `<li>${i}</li>`).join("");
        let actionItemCards = chunk.next.map((step, idx) => `
            <div class="action-item-card">
                <div class="action-item-index">${idx + 1}</div>
                <div style="color:#374151; font-size:0.95em;">${step}</div>
            </div>
        `).join("");

        document.getElementById(`tab-${d.key === "drive" ? "drive" : d.key.split("_")[0]}`).innerHTML = `
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                <h3 style="margin:0; color:#114B43;">${dimTitles[d.key]} Analysis</h3>
                <h4 style="margin:0; color:#4B5563;">Score: ${rawScore}/30</h4>
            </div>
            <p>${chunk.summary}</p>
            <div class="split-flex-row">
                <div class="flex-box-container box-green">
                    <b style="color:#166534;">🟢 Strengths</b>
                    <ul style="margin:10px 0 0 0; padding-left:20px; color:#1E3A1E;">${goodListItems}</ul>
                </div>
                <div class="flex-box-container box-orange">
                    <b style="color:#9A3412;">⚠️ Growth Areas</b>
                    <ul style="margin:10px 0 0 0; padding-left:20px; color:#431407;">${improveListItems}</ul>
                </div>
            </div>
            <h4 style="margin-top:20px; margin-bottom:5px; color:#111827;">Improvement Advice</h4>
            <p style="color:#4B5563; margin-bottom:20px;">${chunk.advice}</p>
            <h4 style="margin-bottom:15px; color:#111827;">Action Steps</h4>
            ${actionItemCards}
        `;
    });

    // 5. Mount Cross-Dimensional System Summaries (Intelligence Generation Layer)
    document.getElementById("overall-analysis-text").innerHTML = `
        Your profile demonstrates a powerful developmental intersection. Your strongest foundational behavioral asset maps directly to your execution score in 
        <b>${dimTitles[highestKey]}</b>, which should be leveraged as an ongoing catalyst tool. Concurrently, your primary strategic improvement priority 
        is situated within developing consistency inside <b>${dimTitles[lowestKey]}</b>. Closing this tracking gap will optimize your operational pacing.
    `;

    document.getElementById("snapshot-summary-para").innerText = `
        Your combined profiling matrix tracks a highly reflective system layout. By consciously linking your natural developmental assets into structured, 
        regular team focus tasks, you can confidently turn high-level internal planning milestones into balanced real-world execution across your peer networks.
    `;
    
    document.getElementById("snapshot-strongest-title").innerText = dimTitles[highestKey];
    document.getElementById("snapshot-weakest-title").innerText = dimTitles[lowestKey];

    // Transition views smoothly
    document.getElementById("quiz-screen").classList.remove("active");
    document.getElementById("dashboard-screen").classList.add("active");
}

// 5. TAB BAR INTERACTION CONTROLLER 
function switchReportTab(event, tabId) {
    // Hide all panels
    const panels = document.querySelectorAll(".report-panel");
    panels.forEach(p => p.classList.remove("active"));

    // Remove status from navigation tab triggers
    const tabs = document.querySelectorAll(".nav-tab");
    tabs.forEach(t => t.classList.remove("active"));

    // Display active components
    document.getElementById(tabId).classList.add("active");
    event.currentTarget.classList.add("active");
}

function restartQuiz() {
    currentQuestionIndex = 0;
    userResponses = {};
    document.getElementById("dashboard-screen").classList.remove("active");
    document.getElementById("onboarding-screen").classList.add("active");
}