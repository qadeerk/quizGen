export default function EvaluateExplanationQuestionComponent({ quiz, onQuestionAnswered }: { quiz: any, onQuestionAnswered: (answered: { answered: any }) => void }) {

    const evaluateExplanation = () => {
        return true;
    };

    function handleExplanationSubmit() {
        if (quiz.type === 'explanation') {
            if (evaluateExplanation()) {
                onQuestionAnswered({ answered: "yes" });
            }
        }
    }
    
    return (
        <div style={{ textAlign: 'center' }}>
            <p>{quiz.question.value}</p>
            <button
                style={{
                    backgroundColor: 'red',
                    borderRadius: '50%',
                    width: '50px',
                    height: '50px',
                    color: 'white',
                    border: 'none',
                    cursor: 'pointer'
                }}
                onClick={() => handleExplanationSubmit()}
            >
                Submit
            </button>
        </div>
    );
}
