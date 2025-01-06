import {useNavigate } from 'react-router-dom';
import styles from './home.module.scss'

export default function Home() {
  const navigate = useNavigate();

  const handleGenerateQuizClick = () => {
    navigate('/generate');
  };

  const steps = [
    { title: "Step 1", description: "Upload the job description." },
    { title: "Step 2", description: "Review and edit the generated quiz." },
    { title: "Step 3", description: "Publish the finalized quiz." },
    { title: "Step 4", description: "Distribute the evaluation link to candidates." },
  ];

  return (
    <div className={styles.pageContainer}>
      <div className={styles.mainContainer}>
        <h1>Streamline Your Corporate Hiring</h1>
        <h2>HireIQ automatically generates aptitude, technical, and behavioral tests from any passage, helping you assess candidates faster and more fairly.</h2>
        <button className={`hc-theme-toggle ${styles.btnHeroSection}`} id="themeToggle" onClick={handleGenerateQuizClick}>Generate Quiz</button>
      </div>
      
      <div className={styles.processHeading}>
        <h2>Steps to follow for quiz</h2>
      </div>
      
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 p-4">
      {steps.map((step, index) => (
        <div
          key={index}
          className="bg-white shadow-md rounded-lg p-6 hover:shadow-lg transition-shadow"
        >
          <h3 className={`text-lg font-bold mb-2 ${styles.stepsTitle}`}>{step.title}</h3>
          <p className="text-gray-600">{step.description}</p>
        </div>
        ))}
      </div>

      <div className={styles.aboutQuiz}>
        <h2>Why Use HireIQ?</h2>
        <p>
          This powerful tool leverages LLMs to create diverse questions, ensuring quick and accurate candidate screening. 
          By automating your aptitude tests, you save time, reduce costs, and maintain fairness in the evaluation process.
        </p>
      </div>

      <div className={styles.footer}>
        all rights reserved
      </div>
  
    </div>
  )}


