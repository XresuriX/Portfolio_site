import { FC, FunctionComponent } from "react";
import { Grid } from "@nextui-org/react";
import Head from 'next/head'
import Image from 'next/image'

export default function Home() {
  return (
    <>
      <Head>
        <title>Leslie Taffe Python software engineer</title>
        <meta name="" content="Portfolio site for Leslie Taffe remote python software engineer" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
        <Grid.Container  className="h-screen w-100% bg-cobalt text-emerald flex grow justify-center p-5" >
          <Grid className="text-center align-middle bg-white " >
            lorem
          </Grid>
          <Grid className="bg-black " >
            lorem
          </Grid>
        </Grid.Container>
    </>
  )
}

