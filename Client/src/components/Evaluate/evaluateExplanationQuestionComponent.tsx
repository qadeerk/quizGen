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
        <div style={{ paddingLeft: '0px'}}>
            			<p style={{ paddingLeft: '0px'}}>{quiz.question.value}</p>
            			<button
                			style={{
                   			 	backgroundColor: '#005a9e',
                    				padding: '5px',
                   				 borderRadius: '50%',
                   				 width: '75px',
                    				height: '75px',
                   				 color: 'white',
                   				 border: '1px solid #002B5B',
                   				 cursor: 'pointer',
                   				 left: '50%',
                    				transform: 'translateX(-50%)'
               				 }}
               				 onClick={() => handleExplanationSubmit()}
            			>
                Submit
            </button>
        </div>
    );
}
