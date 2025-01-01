export type QuizT = {
    question: {
        id: number;
        value: string;
    },
    options: {
        id: number;
        value: string;
    }[],
    answerIndex: number;
}

export interface Option {
    id: number;
    value: string;
}

export interface Question {
    id: number;
    value: string;
}

export interface QuizQuestion {
    type?: string;
    question: Question;
    context?: string;
    options?: Option[];
    answerIndex?: number;
}

export interface Section {
    title: string;
    description: string;
    questions: QuizQuestion[];
}

export interface QuizCollectionT {
    id: string;
    name: string;
    description: string;
    instructions?: string;
    sections: Section[];
}