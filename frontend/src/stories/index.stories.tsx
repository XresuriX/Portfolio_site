import { ComponentMeta, ComponentStory } from "@storybook/react";
import Home from "../pages/index"
import "../styles/globals.css";

export default {
    title: 'My_site',
    component: Home,
   
  } as ComponentMeta<typeof Home>;
  
export const Template: ComponentStory<typeof Home> = (args) => <Home {...args} />;
Template.parameters = {
  layout: 'fullscreen',
};