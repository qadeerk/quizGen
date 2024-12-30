import { useState } from 'react';

interface RadioQuestionProps {
    quiz: any;
    onQuestionAnswered: (answered: { answered: any }) => void;
}

export default function EvaluateRadioQuestionComponent({ quiz, onQuestionAnswered }: RadioQuestionProps) {
    const [selectedOption, setSelectedOption] = useState<number | null>(null);

    const handleOptionChange = (optionId: number) => {
        if (!quiz.type || quiz.type === 'radio') {
            if (evaluateRadio()) {
                onQuestionAnswered({ answered: optionId });
            }
            setSelectedOption(optionId);
        }
    };

    const evaluateRadio = () => {
        return true;
    };

    return (
        <>
            <p>{quiz.question.value}</p>
            {quiz.options.map((option: any, idx: number) => (
                <div key={idx}>
                    <input
                        type="radio"
                        id={`option-${option.id}`}
                        name={`question-${quiz.question.id}`}
                        checked={selectedOption === option.id}
                        onChange={() => handleOptionChange(option.id)}
                    />
                    <label htmlFor={`option-${option.id}`}>{option.value}</label>
                </div>
            ))}
        </>
    );
}
