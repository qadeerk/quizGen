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
        if(localCache[props.id]){
            setQuizCollection(localCache[props.id])
            setStatus("loaded")

        }else{
            requestQuiz(props.id)
            setStatus("loaded")
        }

        async function requestQuiz(id: number) {
            const response = await fetch(`http://localhost:8000/getMockQuiz?id=${id}`)
            const json = await response.json()
            console.log(JSON.parse(json))
            setQuizCollection(JSON.parse(json));
            localCache[id] = JSON.parse(json);
        }

    }, [])

    // if (status === "loading") {
    //     if (quizCollection.length) {
            return (
                <>
                    {/* TODO : question and option can be simple div also */}
                    {quizCollection.map(q =>
                        <div key={q.question.id}>
                            <Question question={q.question.value} />

                            {q.options.map((option) => {
                                return <Option key={option.id} option={option.value} />
                            })}
                        </div>
                    )}
                </>
            )
        // } else {
        //     <div> No quiz found </div>
        // }
    // }

}