import { useState } from 'react'

export default function TestAnswerGenerator() {
  const [question, setQuestion] = useState("")

  return (
    <>
      <div >{/* question */}
      <form >
        <label htmlFor="question">
          Question
          <br></br>
          <input 
          id='question'
          onChange={(e)=>{setQuestion(e.target.value);console.log(question)}}
          value={question}
          placeholder='Enter your question'
          />
        </label>
        <button>submit</button>
      </form>
      </div>
    </>
  )
}