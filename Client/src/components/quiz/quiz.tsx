import { QuizT } from "../../types/quiz"
import { useEffect, useState } from "react"
import { sampleQuiz } from "../../contexts/getSampleQuiz"
import EdiText from 'react-editext'
import "./quiz.css";

const localCache: { [key: string]: QuizT[] } = {};

interface IQuizProps {
    id: string
}

export const Quiz: React.FC<IQuizProps> = (props: IQuizProps) => {
    // const {quizCollection,setQuizCollection} = useState<QuizT[]>(sampleQuiz)
    const [quizCollection, setQuizCollection] = useState<Array<QuizT>>(sampleQuiz)
    const [status, setStatus] = useState<string>("unloaded")
    const [canEditQuiz, setCanEdit] = useState<string>("");

    useEffect(() => {
        setStatus("loading")
        if (localCache[props.id]) {
            setQuizCollection(localCache[props.id])
            setStatus("loaded")

        } else {
            requestQuiz(props.id)
            setStatus("loaded")
        }

        async function requestQuiz(id: String) {
            const response = await fetch(`http://localhost:8000/getQuiz?id=${id}`)
            const json = await response.json()
            console.log(json)
            setQuizCollection(json);
            // localCache[id] = json;
        }

    }, [])


    const handleSave = (val: any) => {
        console.log('Edited Value -> ', val);
        // setValue(val);
    }

    const toggleEdit = () => {
        canEditQuiz === "" ? setCanEdit("canEdit") : setCanEdit("");
    }

    return (
        (status == "loaded" && <div className="hc-container">
            <button id="edit-quiz-btn" className="hc-generate-btn" style={{ float: "right", marginLeft: "20px" }} onClick={() => alert("Work to be done")}>publish</button>
            <button id="edit-quiz-btn" className="hc-generate-btn" onClick={toggleEdit} style={{ float: "right" }}>{canEditQuiz === "" ? "Edit" : "View"}</button>
            {quizCollection.map(q =>
                <div key={q.question.id} style={{ padding: "5px 0" }}>
                    <div style={{ fontWeight: "bold" }}><p>
                        <EdiText type="text" value={q.question.value} onSave={handleSave} editOnViewClick submitOnUnfocus submitOnEnter showButtonsOnHover 
                        canEdit={canEditQuiz != ""}
                        />
                    </p></div>
                    <div style={{ paddingLeft: "10px" }}>
                        {q.options.map((option) => {
                            return (
                                <div key={option.id} className="hc-input-label-container">
                                    <input className="hc-input" type="radio" id={`option-${q.question.id}${option.id.toString()}`} name={`question-${q.question.id}`} value={option.value} />
                                    <label className="hc-label" htmlFor={`option-${q.question.id}${option.id.toString()}${canEditQuiz}`} style={{ paddingLeft: "5px" }}>
                                        <EdiText type="text" value={option.value} onSave={handleSave} editOnViewClick submitOnUnfocus submitOnEnter showButtonsOnHover />
                                    </label>
                                </div>
                            )
                        })}
                    </div>
                </div>
            )}
        </div>)
    )

}             
