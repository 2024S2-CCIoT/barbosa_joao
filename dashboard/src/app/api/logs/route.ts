"use server";

import { NextResponse } from "next/server";
import { client } from "@/services/mongo";

const DB_NAME = "x4glass";
const LOGS_COLLECTION = "sensor_log";

export async function GET() {
  const db = await client.db(DB_NAME);

  const logsData = await db
    .collection(LOGS_COLLECTION)
    .aggregate([
      {
        $group: {
          _id: "$sensor",
          readings: {
            $push: {
              reading: "$reading",
              date: "$date",
            },
          },
        },
      },
      {
        $sort: { _id: 1 }
      }
    ])
    .toArray();

  return NextResponse.json(logsData);
}
