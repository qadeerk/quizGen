import { ComponentProps } from "react";
import clsx from 'clsx';
import styles from './button.module.css';

export type ButtonProps = ComponentProps<'button'> & {
    variant?: 'primary' | 'secondary'| 'destructive';
    size? : 'small' | 'medium' | 'large';
}
export const Button  = ({variant = "primary" , size = "small" , ...props }:ButtonProps) => {    
    let className = clsx(styles.button,styles.small, {
        [styles['button-secondary']]: variant === 'secondary',
        [styles['button-destructive']]: variant === 'destructive',
        [styles['medium']]: size === "medium",
        [styles['large']]: size === "large",
    });

    return <button className={className} {...props} ></button> 
}