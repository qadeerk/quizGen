import { Quiz } from '../components/quiz/quiz'
import './app.css'
import AppHeader from '../components/Header'
import QuizGenerator from '../components/quizGenerator/quizGenerator'
import { useState } from 'react'
import ReactMarkdown from "react-markdown";

function App() {
  const [quizId, setQuizId] = useState<number>(0)
  const [matchingAttributes, setMatchingAttributes] = useState<string>("")
  const [uniqueAttributes, setuniqueAttributes] = useState<string>("")

  return (
    <>
      <AppHeader />
      <QuizGenerator setQuizId={setQuizId} setMatchingAttributes={setMatchingAttributes}  setuniqueAttributes={setuniqueAttributes} />
      {/* <div className="hc-container">
      <EdiText type="text" value={value} onSave={handleSave} editOnViewClick submitOnUnfocus submitOnEnter showButtonsOnHover/>
      </div> */}
      {quizId != 0 ? <Quiz id={quizId}></Quiz> : null}
      <div className="hc-container">
          <ReactMarkdown>{matchingAttributes}</ReactMarkdown>
      </div>
      <div className="hc-container">
          <ReactMarkdown>{uniqueAttributes}</ReactMarkdown>
      </div>
    </>
  )
}

export default App
