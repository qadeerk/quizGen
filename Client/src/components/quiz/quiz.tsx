import Question from "../question/question"
import { Option } from "../option/option"
import { QuizT } from "../../types/quiz"
import { useEffect, useState } from "react"
import { sampleQuiz } from "../../contexts/getSampleQuiz"

const localCache: { [key: number]: QuizT[] } = {};

interface IQuizProps {
    id: number
}

export const Quiz: React.FC<IQuizProps> = (props: IQuizProps) => {
    // const {quizCollection,setQuizCollection} = useState<QuizT[]>(sampleQuiz)
    const [quizCollection, setQuizCollection] = useState<Array<QuizT>>(sampleQuiz)
    const [status, setStatus] = useState<string>("unloaded")

    useEffect(() => {
        // requestQuiz()
        setStatus("loading")
        if (localCache[props.id]) {
            setQuizCollection(localCache[props.id])
            setStatus("loaded")

        } else {
            requestQuiz(props.id)
            setStatus("loaded")
        }

        async function requestQuiz(id: number) {
            const response = await fetch(`http://localhost:8000/getQuiz?id=${id}`)
            const json = await response.json()
            console.log(json)
            setQuizCollection(json);
            localCache[id] = json;
        }

    }, [])


    return (
        <div className="hc-container">
            {/* TODO : question and option can be simple div also */}
            {quizCollection.map(q =>
                <div key={q.question.id} style={{ padding: "5px 0" }}>
                    <Question question={q.question.value} />
                    <div style={{ paddingLeft: "10px" }}>
                        {q.options.map((option) => {
                            return (
                                <div key={option.id}>
                                    <input type="radio" id={option.id.toString()} name={`question-${q.question.id}`} value={option.value} />
                                    <label htmlFor={option.id.toString()} style={{ paddingLeft: "5px" }}>{option.value}</label>
                                </div>
                            )
                        })}
                    </div>
                </div>
            )}
        </div>
    )

}             
