import MainLayout from "../layouts/MainLayout";
import { NextPageWithLayout } from "./_app";

const AboutPage: NextPageWithLayout = () => {
  return <div className="p-10 text-8xl font-bold underline">About</div>;
};

AboutPage.getLayout = (page) => {
  return <MainLayout>{page}</MainLayout>;
};

export default AboutPage;
