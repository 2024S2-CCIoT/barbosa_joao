"use client";

import { useQuery } from "@tanstack/react-query";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  ChartData,
} from "chart.js";
import { Line } from "react-chartjs-2";
import { format } from "date-fns";
import { withQuery } from "@/hocs/withQuery";

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

const options = {
  responsive: true,
  plugins: {
    legend: {
      position: "top" as const,
    },
    title: {
      display: true,
      text: "Leitura dos sensores",
    },
  },
};

const Home = () => {
  const { data, error, isLoading } = useQuery({
    queryKey: ["logs"],
    queryFn: async () => (await fetch("/api/logs")).json(),
  });

  if (error) return <div>Erro</div>;
  if (isLoading) return <div>Carregando</div>;

  const chart = (
    sensorName: string
  ): ChartData<
    "line",
    Record<string, any> | Record<string, any>[],
    string
  > => ({
    labels: data
      .filter((x: any) => x._id === sensorName)
      .flatMap((x: any) => {
        return x.readings.map((x: any) =>
          format(new Date(x.date), "dd/M/yyyy hh:mm:ss")
        );
      }),
    datasets: [
      {
        label: sensorName,
        data: data
          .filter((x: any) => x._id === sensorName)
          .flatMap((x: any) => {
            return x.readings.map((x: any) => x.reading);
          }),
        borderColor: "#FF5C00",
        backgroundColor: "black",
        borderWidth: 2,
        pointBorderColor: "white",
        pointBorderWidth: 1,
      },
    ],
  });

  return (
    <div className="grid grid-cols-1 gap-10">
      {data.map((sensor: any, idx: number) => (
        <span key={idx} className="px-24">
          <Line options={options} data={chart(sensor._id)} />
        </span>
      ))}
    </div>
  );
};

export default withQuery(Home);
