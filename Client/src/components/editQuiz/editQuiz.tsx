import { QuizCollectionT, QuizQuestion } from "../../types/quiz"
import { useEffect, useState } from "react"
import EdiText from 'react-editext'
import "./editQuiz.scss";
import { useNavigate, useSearchParams } from "react-router-dom";
import { Button } from "../button/button";

interface IQuizProps {
    id: string
}

const quizzes = [
    // Sample quizzes data
    {
        id: "530ba1eb-6968-4afc-b980-5da21c597c14",
        name: 'Sample Quiz 1',
        description: 'This is a sample quiz description.',
        instructions: 'Please read the instructions carefully before starting the quiz.',
        sections: [
            {
                title: 'Section 1',
                description: 'This is a sample quiz description an what is included in the next desction 1',
                questions: [{ "type": "radio", "question": { "id": 0, "value": "What do work ethics encompass?" }, "options": [{ "id": 0, "value": "Technical skills and knowledge specific to a job" }, { "id": 1, "value": "Personal interests and hobbies of an employee" }, { "id": 2, "value": "Company policies and procedures for employee conduct" }, { "id": 3, "value": "Moral principles and values like reliability, honesty, fairness, and commitment." }], "answerIndex": 3 }, { "question": { "id": 1, "value": "What is a key component of a strong work ethic?" }, "options": [{ "id": 0, "value": "Procrastination" }, { "id": 1, "value": "Disorganization" }, { "id": 2, "value": "Neglect" }, { "id": 3, "value": "Accountability." }], "answerIndex": 3 }, { "question": { "id": 2, "value": "What are the key factors that promote a positive workplace environment?" }, "options": [{ "id": 0, "value": "Competition, secrecy, and favoritism" }, { "id": 1, "value": "Isolation, rigidity, and unpredictability" }, { "id": 2, "value": "Negativity, dishonesty, and ambiguity" }, { "id": 3, "value": "Honesty, transparency, and fairness." }], "answerIndex": 3 }]
            },
            {
                title: 'Section 2',
                description: 'This is a sample quiz description an what is included in the next desction 2',
                questions: [{ "type": "explanation", "question": { "id": 0, "value": "What do work ethics encompass?" }, "context": "Work ethics encompass the set of moral principles and values—such as honesty, integrity, accountability, respect, reliability, and fairness—that guide individuals to act responsibly, uphold high standards, and contribute positively within a professional environment." }, { "type": "radio", "question": { "id": 1, "value": "2.What is a key component of a strong work ethic?" }, "options": [{ "id": 0, "value": "Procrastination" }, { "id": 1, "value": "Disorganization" }, { "id": 2, "value": "Neglect" }, { "id": 3, "value": "Accountability." }], "answerIndex": 3 }, { "type": "radio", "question": { "id": 2, "value": "3.What are the key factors that promote a positive workplace environment?" }, "options": [{ "id": 0, "value": "Competition, secrecy, and favoritism" }, { "id": 1, "value": "Isolation, rigidity, and unpredictability" }, { "id": 2, "value": "Negativity, dishonesty, and ambiguity" }, { "id": 3, "value": "Honesty, transparency, and fairness." }], "answerIndex": 3 }]
            }
        ]
    }
];

export default function EditQuiz() {
    const navigate = useNavigate();
    const [searchParams] = useSearchParams();
    const quizId = searchParams.get('quizId');
    const quizIdParam = quizId ? quizId : "";
    const [quizCollection, setQuizCollection] = useState<Array<QuizCollectionT>>(quizzes)
    const [status, setStatus] = useState<string>("unloaded")
    const [canEditQuiz, setCanEdit] = useState<string>("");

    useEffect(() => {
        async function requestQuiz(id: String) {
            try {
                const response = await fetch(`http://localhost:8000/getQuiz?id=${id}`)
                if (!response.ok) {
                    throw new Error("Network response was not ok");
                }
                const json = await response.json();
                if (!json || !json.id) {
                    throw new Error("Invalid quiz data");
                }
                setQuizCollection([json]);
                setStatus("loaded");
                setCanEdit("canEdit");
            } catch (e) {
                console.error(e);
                setStatus("notFound");
            }
        }
        requestQuiz(quizIdParam);
    }, [])

    if (status === "notFound") {
        return <div>Quiz not found</div>;
    }

    const handleSave = (val: any, sectionIndex: number, questionId: number, optionId?: number, isContext?: boolean) => {
        let updatedQuizCollection;
        updatedQuizCollection = quizCollection.map((quiz) => {
            quiz.sections[sectionIndex].questions = quiz.sections[sectionIndex].questions.map((question) => {
                if (question.question.id === questionId) {
                    if (isContext) {
                        question.context = val;
                    } else if (optionId !== undefined) {
                        question.options = question.options ? question.options.map((option) => {
                            if (option.id === optionId) {
                                option.value = val;
                            }
                            return option;
                        }) : [];
                    } else {
                        question.question.value = val;
                    }
                }
                return question;
            });
            return quiz;
        });
        setQuizCollection(updatedQuizCollection);
    }

    const handleSaveFields = (
        val: any,
        sectionIndex?: number,
        name?: string,
        description?: string,
        title?: string,
        instructions?: string
    ) => {
        let updatedQuizCollection = quizCollection.map((quiz) => {
            if (sectionIndex !== undefined && quiz.sections[sectionIndex]) {
                if (title) {
                    quiz.sections[sectionIndex].title = val;
                } else if (description) {
                    quiz.sections[sectionIndex].description = val;
                }
            } else {
                if (name) {
                    quiz.name = val;
                } else if (description) {
                    quiz.description = val;
                } else if (instructions) {
                    quiz.instructions = val;
                }
            }
            return quiz;
        });
        setQuizCollection(updatedQuizCollection);
    };

    const renderRadioQuestion = (q: QuizQuestion, sectionIndex: number) => {
        return (status == "loaded" &&
            <div key={q.question.id} className="radio-question">
                <div className="question-text">
                    <EdiText type="text" value={q.question.value} onSave={(val) => handleSave(val, sectionIndex, q.question.id)} editOnViewClick submitOnUnfocus submitOnEnter showButtonsOnHover
                        canEdit={canEditQuiz !== ""} viewProps={{ className: "radio-question-text" }} />
                </div>
                <div className="options-container">
                    {q.options && q.options.map((option) => {
                        return (
                            <div key={option.id} className="hc-input-label-container">
                                <input className="hc-input" type="radio" id={`option-${q.question.id}${option.id.toString()}${sectionIndex}`} name={`question-${q.question.id}${sectionIndex}`}
                                    value={option.value}
                                    checked={option.id === q.answerIndex} // Use answerIndex to set checked
                                    onChange={() => handleOptionChange(sectionIndex, q.question.id, option.id)}
                                />
                                <label className="hc-label" htmlFor={`option-${q.question.id}${option.id.toString()}${sectionIndex}${canEditQuiz}`} style={{ paddingLeft: "5px" }} >
                                    <EdiText type="text" value={option.value} onSave={(val) => handleSave(val, sectionIndex, q.question.id, option.id)} editOnViewClick submitOnUnfocus submitOnEnter showButtonsOnHover viewProps={{ className: "radio-option-text" }} />
                                </label>
                            </div>
                        );
                    })}
                </div>
            </div>
        );
    }

    const renderExplainationQuestion = (q: QuizQuestion, sectionIndex: number) => {
        return (
            <div key={q.question.id} className="explanation-question">
                <div className="question-text">
                    <EdiText type="text" value={q.question.value} onSave={(val) => handleSave(val, sectionIndex, q.question.id)} editOnViewClick submitOnUnfocus submitOnEnter showButtonsOnHover
                        canEdit={canEditQuiz !== ""} viewProps={{ className: "explanation-question-text" }} />
                </div>
                <div>
                    <p>Context</p>
                    {q.context && <EdiText type="textarea" value={q.context} onSave={(val) => handleSave(val, sectionIndex, q.question.id, undefined, true)} editOnViewClick submitOnUnfocus submitOnEnter showButtonsOnHover
                        canEdit={canEditQuiz !== ""} />
                    }
                </div>
            </div>
        );
    }
    const handleOptionChange = (sectionIndex: number, questionId: number, optionId: number) => {
        const updatedQuizCollection = quizCollection.map((quiz) => {
            quiz.sections[sectionIndex].questions = quiz.sections[sectionIndex].questions.map((question) => {
                if (question.question.id === questionId) {
                    question.answerIndex = optionId;
                }
                return question;
            });
            return quiz;
        });
        setQuizCollection(updatedQuizCollection);
    }

    const addQuestionToSection = (sectionIndex: number, question: QuizQuestion) => {
        setQuizCollection(prevQuizzes => {
            return prevQuizzes.map(quiz => {
                const updatedSections = quiz.sections.map((section, idx) => {
                    if (idx === sectionIndex) {
                        return {
                            ...section,
                            questions: [...section.questions, question]
                        };
                    }
                    return section;
                });
                return { ...quiz, sections: updatedSections };
            });
        });
    }

    const handleAddQuestion = (sectionIndex: number) => {
        const questionType = prompt("Enter question type: 'explanation' or 'radio'");
        if (questionType === "explanation") {
            addQuestionToSection(sectionIndex, {
                type: "explanation",
                question: { id: Math.random(), value: "New explanation question" },
                context: "New context..."
            });
        } else if (questionType === "radio") {
            addQuestionToSection(sectionIndex, {
                type: "radio",
                question: { id: Math.random(), value: "New radio question" },
                options: [
                    { id: 0, value: "option 1" },
                    { id: 1, value: "option 2" },
                    { id: 2, value: "option 3" },
                    { id: 3, value: "option 4" }
                ],
                answerIndex: 0
            });
        }
    };

    const handleAddSection = () => {
        setQuizCollection(prevQuizzes => {
            return prevQuizzes.map(quiz => {
                return {
                    ...quiz,
                    sections: [
                        ...quiz.sections,
                        {
                            title: "New Section Title",
                            description: "New Section Description",
                            questions: []
                        }
                    ]
                };
            });
        });
    };

    const renderInfoPannel = (
        type?: string,
        title?: string,
        description?: string,
        instructions?: string) => {
        return (
            <div className="info-panel">
                {title && <EdiText type="text" value={title} onSave={(val) => handleSaveFields(val, undefined, "name")} editOnViewClick submitOnUnfocus submitOnEnter showButtonsOnHover canEdit={canEditQuiz !== ""} viewProps={{ className: "quiz-title" }} />}
                {description && <EdiText type="text" value={description} onSave={(val) => handleSaveFields(val, undefined, undefined, "description")} editOnViewClick submitOnUnfocus submitOnEnter showButtonsOnHover canEdit={canEditQuiz !== ""} viewProps={{ className: "quiz-description" }} />}
                {instructions && <EdiText type="text" value={instructions} onSave={(val) => handleSaveFields(val, undefined, undefined, undefined, undefined, "instructions")} editOnViewClick submitOnUnfocus submitOnEnter showButtonsOnHover canEdit={canEditQuiz !== ""} viewProps={{ className: "quiz-instructions" }} />}
            </div>
        );
    }

    const renderSection = (section: any, sectionIndex: number) => {
        return (
            <div key={sectionIndex} className="section">
                {section.title && <EdiText type="text" value={section.title} onSave={(val) => handleSaveFields(val, sectionIndex, undefined, undefined, "title")} editOnViewClick submitOnUnfocus submitOnEnter showButtonsOnHover canEdit={canEditQuiz !== ""} viewProps={{ className: "section-title-text" }} />}
                {section.description && <EdiText type="text" value={section.description} onSave={(val) => handleSaveFields(val, sectionIndex, undefined, "description")} editOnViewClick submitOnUnfocus submitOnEnter showButtonsOnHover canEdit={canEditQuiz !== ""} viewProps={{ className: "section-description-text" }} />}
                {section.questions.map((question: QuizQuestion, questionIndex: number) => {
                    if (question.type === "radio" || !question.type) {
                        return renderRadioQuestion(question, sectionIndex);
                    } else if (question.type === "explanation") {
                        return renderExplainationQuestion(question, sectionIndex);
                    }
                    return null;
                })}
                <Button onClick={() => handleAddQuestion(sectionIndex)}>Add Question</Button>
            </div>
        );
    }

    const publishQuiz = async () => {
        try {

            const formData = new FormData();
            formData.append("id",quizIdParam);
            formData.append("quiz",JSON.stringify(quizCollection[0]));

            const response = await fetch("http://localhost:8000/publishQuiz", {
                method: "POST",
                body: formData,
                redirect: "follow"
              });

            if (!response.ok) {
                throw new Error("Failed to publish quiz");
            }

            navigate('/publish?quizId=' + quizIdParam);
        } catch (error) {
            console.error("Error publishing quiz:", error);
        }
    };

    return (
        (status == "loaded" &&
            <div className="quiz-page-container">
                <div className="publish-container">
                    <Button id="edit-quiz-btn" className="hc-generate-btn" onClick={publishQuiz}>
                        publish
                    </Button>
                </div>
                {quizCollection.map((quiz, quizIndex) => (
                    <div key={quizIndex} className="quiz-container">
                        <div className="info-panel-container">
                            {renderInfoPannel("primary", quiz.name, quiz.description, quiz.instructions)}
                        </div>

                        <div className="sections-container">
                            {quiz.sections.map((section, sectionIndex) => (
                                <div key={sectionIndex} className="section-container">
                                    {renderSection(section, sectionIndex)}
                                </div>
                            ))}
                        </div>
                        <Button onClick={handleAddSection}>Add Section</Button>
                    </div>
                ))}
            </div>
        )
    )

}
