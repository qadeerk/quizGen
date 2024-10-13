
type QuestionT = Readonly<{
    question: string;
}>

export default function Question({question}:QuestionT){
    return <div><p>{question}</p></div>
}