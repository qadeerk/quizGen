import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './button';

const meta: Meta = {
    title: 'Button',
    component: Button,
    args: {
        children: 'Button',
        disabled: false,
    },
    argTypes: {
        disabled: {
            control: 'boolean',
            description: 'Disables the button',
        },
        variant: {
            control: {
                type: 'select',
            },
            description: 'Changes the button style',
        },
        size: {
            control: {
                type: 'select',
            },
            description: 'Changes the button size',
        },
        onClick: {
            action: 'clicked',
        },
    },
}

export default meta;
type Story = StoryObj<typeof Button>;

export const Primary: Story = {
    args: {
        variant: 'primary',
    },
};
export const Secondary: Story = {
    args: {
        ...Primary.args,
        variant: 'secondary',
    },
};

export const Destructive: Story = {
    args: {
        variant: 'destructive',
    },
};