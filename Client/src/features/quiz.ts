import {createSlice, PayloadAction} from '@reduxjs/toolkit';
import { QuizT } from '../types/quiz';
import { sampleQuiz } from "../contexts/getSampleQuiz"

export  type QuizState = {
    entities: QuizT[];
    processing: boolean;
}

const initialState: QuizState = {
    entities: [],
    processing: true,
}

const quizSlice = createSlice({
    name:'quiz',
    initialState,
    reducers: {
        addQuiz: (state, actions: PayloadAction<QuizT[]>) => {
            state.entities = actions.payload;
        },
        fetchQuiz: (state) => state,
        editQuiz: (state) => state,
        deleteQuiz: (state) => state,
        updateQuiz: (state) => state,
    }
})

quizSlice.actions.addQuiz(sampleQuiz)