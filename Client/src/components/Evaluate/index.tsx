import styles from './evaluate.module.css';
import { useState, useMemo, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import { Button } from '../../../../RealtimeServer/src/components/button/Button';
import EvaluationQuestion from './evaluationQuestion';
import EvaluationPanel from './evaluationPanel';

export default function Evaluate() {
  const [searchParams] = useSearchParams();
  const quizId = searchParams.get('quizId');
  const quizIdParam = quizId ? quizId : NaN;
  const [currentSectionIndex, setCurrentSectionIndex] = useState(0);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [started, setStarted] = useState(false);
  const [questionAnswered, setQuestionAnswered] = useState<{ answered: any } | null>(null);
  const [showAnswerMessage, setShowAnswerMessage] = useState(false);
  const [quizCompleted, setQuizCompleted] = useState(false);
  const [showSectionStart, setShowSectionStart] = useState(true);
  const [answers, setAnswers] = useState<{ [key: string]: any }>({});

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
          questions: [{ "type": "explanation", "question": { "id": 0, "value": "1.What do work ethics encompass?" }, "options": [{ "id": 0, "value": "Technical skills and knowledge specific to a job" }, { "id": 1, "value": "Personal interests and hobbies of an employee" }, { "id": 2, "value": "Company policies and procedures for employee conduct" }, { "id": 3, "value": "Moral principles and values like reliability, honesty, fairness, and commitment." }], "answerIndex": 3 }, { "question": { "id": 1, "value": "2.What is a key component of a strong work ethic?" }, "options": [{ "id": 0, "value": "Procrastination" }, { "id": 1, "value": "Disorganization" }, { "id": 2, "value": "Neglect" }, { "id": 3, "value": "Accountability." }], "answerIndex": 3 }, { "question": { "id": 2, "value": "3.What are the key factors that promote a positive workplace environment?" }, "options": [{ "id": 0, "value": "Competition, secrecy, and favoritism" }, { "id": 1, "value": "Isolation, rigidity, and unpredictability" }, { "id": 2, "value": "Negativity, dishonesty, and ambiguity" }, { "id": 3, "value": "Honesty, transparency, and fairness." }], "answerIndex": 3 }]
        }
      ]
    }
  ];

  const quiz = quizzes.find(q => q.id === quizIdParam);

  if (!quizIdParam || !quiz) {
    return (
      <div className={styles.contentWrapper}>
        <div className={styles.evaluateContainer}>
          <EvaluationPanel
            type="tertiary"
            title="Quiz not found"
            description="The quiz you are looking for does not exist."
          />
        </div>
      </div>
    );
  }

  const handleStartQuiz = () => {
    setStarted(true);
    setCurrentSectionIndex(0);
    setCurrentQuestionIndex(0);
    setShowSectionStart(true);
  };

  const handleStartSection = () => {
    setShowSectionStart(false);
  };

  const handleNext = () => {
    if (!questionAnswered) {
      setShowAnswerMessage(false);
      setTimeout(() => setShowAnswerMessage(true), 0);
      return;
    }
    setShowAnswerMessage(false);

    // Store the answered question in the answers state
    const currentSection = quiz?.sections[currentSectionIndex];
    if (currentSection) { // TODO : last question answered is not stored
      const questionKey = `${currentSectionIndex}-${currentQuestionIndex}`;
      console.log('questionKey', questionKey);
      setAnswers(prevAnswers => ({
        ...prevAnswers,
        [questionKey]: questionAnswered
      }));
    }

    if (currentQuestionIndex < currentSection.questions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else if (currentSectionIndex < quiz.sections.length - 1) {
      setShowSectionStart(true);
      setCurrentSectionIndex(currentSectionIndex + 1);
      setCurrentQuestionIndex(0);
    } else {
      setQuizCompleted(true);
    }
    setQuestionAnswered(null);
  };

  useEffect(() => {
    console.log(answers);
  }, [answers,quizCompleted]);

  const renderEvaluationQuestion = useMemo(() => {
    return (
      <EvaluationQuestion
        key={`${currentSectionIndex}-${currentQuestionIndex}`}
        quiz={quiz.sections[currentSectionIndex].questions[currentQuestionIndex]}
        onQuestionAnswered={setQuestionAnswered}
      />
    );
  }, [currentSectionIndex, currentQuestionIndex]);

  return (
    <div className={styles.contentWrapper}>
      <div className={styles.evaluateContainer}>
        {!started ? (
          <EvaluationPanel
            type="main"
            title={quiz.name}
            description={quiz.description}
            instructions={quiz.instructions}
            buttonText="Start Quiz"
            buttonAction={handleStartQuiz}
          />
        ) : quizCompleted ? (
          <EvaluationPanel
            type="tertiary"
            title="Thank you for your submission!"
            description="We will contact you soon."
          />
        ) : showSectionStart ? (
          <EvaluationPanel
            type="secondary"
            title={quiz.sections[currentSectionIndex].title}
            description={quiz.sections[currentSectionIndex].description}
            buttonText="Start Section"
            buttonAction={handleStartSection}
          />
        ) : (
          <div className={styles.quizContent}>
            {quiz.sections[currentSectionIndex] && (
              <>
                <h2>{quiz.sections[currentSectionIndex].title}</h2>
                {renderEvaluationQuestion}
                <div style={{ display: 'flex', alignItems: 'center' }}>
                  <Button label="Next" onClick={handleNext} />
                  {showAnswerMessage && !questionAnswered && <p className={styles.showAnswerMessage}>Please answers the question before proceeding.</p>}
                </div>
              </>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
