import { Quiz } from '../components/quiz/quiz'
import './app.css'
import AppHeader from '../components/Header'
import QuizGenerator from '../components/quizGenerator/quizGenerator'
import { useState } from 'react'
import { BrowserRouter, Routes, Route, useSearchParams } from 'react-router-dom';
import Home from '../components/Home';
import Evaluate from '../components/Evaluate';
import Report from '../components/Report';

function EditQuiz() {
  const [searchParams] = useSearchParams();
  const quizId = searchParams.get('quizId');
  return quizId ? <Quiz id={quizId} /> : <div>Invalid link</div>;
}

function App() {
  // @ts-ignore
  const [quizId, setQuizId] = useState<number>(0)
  // @ts-ignore
  const [matchingAttributes, setMatchingAttributes] = useState<string>("")
  // @ts-ignore
  const [uniqueAttributes, setUniqueAttributes] = useState<string>("")

  return (
    <>
      <BrowserRouter>
        <AppHeader />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/generate" element={
            <QuizGenerator
              setQuizId={setQuizId}
              setMatchingAttributes={setMatchingAttributes}
              setUniqueAttributes={setUniqueAttributes}
            />
          } />
          <Route path="/edit" element={<EditQuiz />} />
          <Route path="/evaluation" element={<Evaluate />} />
          <Route path="/report" element={<Report />} />
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
