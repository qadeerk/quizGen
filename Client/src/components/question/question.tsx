
type QuestionT = Readonly<{
    question: string;
}>

export default function Question({question}:QuestionT){
    return <div style={{ fontWeight: "bold"}}><p>{question}</p></div>
}