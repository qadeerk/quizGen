
import TestAnswerGenerator from '../components/testAnswerGenerator/testAnswerGenerator'
import { Quiz } from '../components/quiz/quiz'

import './app.css'

function App() {

  return (
    <>
      <h1 className="text-3xl underline">
      Quiz Gen
      </h1>
      <TestAnswerGenerator />
      <Quiz id={1}></Quiz>
    </>
  )
}

export default App
