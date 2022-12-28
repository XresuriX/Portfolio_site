import { NextPage } from 'next'
import { AppProps } from 'next/app'
import { FC, ReactElement } from 'react'
import '../styles/globals.css'

type NextPageWithLayout<P = { }, IP = P> = NextPage<P, IP> & {
  getLayout?(page: ReactElement): ReactElement
}

type AppPropsWithLayout = AppProps & {
  Component: NextPageWithLayout
}

const App: FC<AppPropsWithLayout> = ({ Component, pageProps }) => {
  const getLayout = Component.getLayout ?? ((page) => page)
  
  return getLayout(<Component {...pageProps} />)
}

export default App

export type { NextPageWithLayout }
