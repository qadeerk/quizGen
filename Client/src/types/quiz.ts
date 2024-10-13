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