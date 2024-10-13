
type OptionProps = Readonly<{
    option: string;
}> 

export const Option  = ({option}:OptionProps) => {
    return <div><p>{option}</p></div>
}