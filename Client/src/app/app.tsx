
import TestAnswerGenerator from '../components/testAnswerGenerator/testAnswerGenerator'
import { Quiz } from '../components/quiz/quiz'

import './app.css'

import AppHeader from '../components/Header'
import QuizGenerator from '../components/quizGenerator/quizGenerator'
import { useState } from 'react'

function App() {
  const [quizId, setQuizId] = useState<number>(0)

  return (
    <>
      <AppHeader /> 
      <QuizGenerator setQuizId={setQuizId}/>

      {quizId != 0 ? <Quiz id={quizId}></Quiz> : null}

      {/* <h1 className="text-3xl underline">
      Quiz Gen
      </h1>
      <TestAnswerGenerator />
      <Quiz id={quizId}></Quiz> */}
    </>
  )
}

export default App
