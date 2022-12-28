import Link from "next/link";
import MainLayout from "../layouts/MainLayout";
import { NextPageWithLayout } from "./_app";

const IndexPage: NextPageWithLayout = () => {
  return (
    <>
      <div className="text-3xl text-blue-200 font-bold ">Hello World</div>

      <div>
        Go to <Link href="/about">about page</Link>
      </div>
    </>
  );
};

IndexPage.getLayout = (page) => {
  return <MainLayout>{page}</MainLayout>;
};

export default IndexPage;
