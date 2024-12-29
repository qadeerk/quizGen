import { useState, useEffect } from 'react';

interface QuestionProps {
    quiz: any;
    onQuestionAnswered: (answered: boolean) => void;
}

export default function EvaluationQuestion({ quiz, onQuestionAnswered }: QuestionProps) {
    const [selectedOption, setSelectedOption] = useState<number | null>(null);
    const randomKey = Math.floor(1000 + Math.random() * 9000);

    useEffect(() => {
        setSelectedOption(null);
        console.log('EvaluationQuestion rendered');
    }, []);

    const handleOptionChange = (optionId: number) => {
        if (!quiz.type || quiz.type === 'radio') {
            if(evaluateRadio(optionId)){
                onQuestionAnswered(true);
            }
            setSelectedOption(optionId);
        }
    };

    const evaluateRadio = (optionId: number) => {
        return true;
        // Add evaluation logic here
        // console.log(`Option ${optionId} selected`);
    };

    return (
        <div>
            <p>{quiz.question.value}</p>
            {quiz.options.map((option: any, idx: number) => (
                <div key={idx+randomKey}>
                    <input
                        type="radio"
                        id={`option-${option.id}`}
                        name={`question-${quiz.question.id}-${randomKey}`}
                        checked={selectedOption === option.id}
                        onChange={() => handleOptionChange(option.id)}
                    />
                    <label htmlFor={`option-${option.id}`}>{option.value}</label>
                </div>
            ))}
        </div>
    );
}
