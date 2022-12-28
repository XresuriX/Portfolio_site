import { FC, ReactNode } from "react";

type MainLayoutContentProps = {
  children: ReactNode
}

const MainLayoutContent: FC<MainLayoutContentProps> = ({ children }) => {
  return (
    <div>
      <div>MainLayout</div>

      {children}
    </div>
  )
}

type MainLayoutProps = {
  children: ReactNode
}

const MainLayout: FC<MainLayoutProps> = ({ children }) => {
  return (
    <MainLayoutContent>
      {children}
    </MainLayoutContent>
  )
}

export default MainLayout
