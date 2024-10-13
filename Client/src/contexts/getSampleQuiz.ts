
/** 
 * context is the qrong place to put this
 */

import { QuizT } from "../types/quiz";

export const sampleQuiz:Array<QuizT> = [
    {
        question: {
            id: 1,
            value:"What is the capital of France?"
        },
        options: [{id:5,value:"New York"}, {id:2,value:"London"}, {id:3,value:"Paris"}, {id:4,value:"Dublin"}],
        answerIndex: 2,
    },
    {
        question: {
            id: 2,
            value:"What is the capital of Spain?"},
        options: [{id:1,value:"Berlin"}, {id:2,value:"Madrid"}, {id:3,value:"Rome"}, {id:4,value:"Lisbon"}],
        answerIndex: 1,
    },
    {
        question: {
            id: 3,
            value:"What is the capital of Portugal?"},
        options: [{id:1,value:"Paris"}, {id:2,value:"Lisbon"}, {id:3,value:"Madrid"}, {id:4,value:"DubRomelin"}],
        answerIndex: 1,
    }
]
