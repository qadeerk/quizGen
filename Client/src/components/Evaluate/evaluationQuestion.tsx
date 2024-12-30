import EvaluateExplanationQuestionComponent from './evaluateExplanationQuestionComponent';
import EvaluateRadioQuestionComponent from './evaluateRadioQuestion';

interface QuestionProps {
    quiz: any;
    onQuestionAnswered: (answered: { answered: any }) => void;
}

export default function EvaluationQuestion({ quiz, onQuestionAnswered }: QuestionProps) {
    return (
        <div>
            {quiz.type === 'explanation' ? (
                <EvaluateExplanationQuestionComponent quiz={quiz} onQuestionAnswered={onQuestionAnswered} />
            ) : (
                <EvaluateRadioQuestionComponent quiz={quiz} onQuestionAnswered={onQuestionAnswered} />
            )}
        </div>
    );
}

