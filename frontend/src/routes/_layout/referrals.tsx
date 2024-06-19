import {
  Container,
  Flex,
  Heading,
  Skeleton,
  Table,
  TableContainer,
  Tbody,
  Td,
  Th,
  Thead,
  Tr,
} from "@chakra-ui/react"
import { useSuspenseQuery } from "@tanstack/react-query"
import { createFileRoute } from "@tanstack/react-router"

import { Suspense } from "react"
import { ErrorBoundary } from "react-error-boundary"
import { ReferralsService } from "../../client"
import ActionsMenu from "../../components/Common/ActionsMenu"
import Navbar from "../../components/Common/Navbar"

export const Route = createFileRoute("/_layout/referrals")({
  component: Referrals,
})

function ReferralsTableBody() {
  const { data: referrals } = useSuspenseQuery({
    queryKey: ["referrals"],
    queryFn: () => ReferralsService.readReferrals({}),
  })

  return (
    <Tbody>
      {referrals.data.map((referral) => (
        <Tr key={referral.id}>
          <Td>{referral.id}</Td>
          <Td>{referral.source_id}</Td>
          <Td color={!referral.source_id ? "ui.dim" : "inherit"}>
            {referral.source_id || "N/A"}
          </Td>
         
          <Td>
            <ActionsMenu type={"Referral"} value={referral} />
          </Td>
        </Tr>
      ))}
    </Tbody>
  )
}
function ReferralsTable() {
  return (
    <TableContainer>
      <Table size={{ base: "sm", md: "md" }}>
        <Thead>
          <Tr>
            <Th>ID</Th>
            <Th>Source ID</Th>
            <Th>Last Name</Th>
           
            <Th>Actions</Th>
          </Tr>
        </Thead>
        <ErrorBoundary
          fallbackRender={({ error }) => (
            <Tbody>
              <Tr>
                <Td colSpan={4}>Something went wrong: {error.message}</Td>
              </Tr>
            </Tbody>
          )}
        >
          <Suspense
            fallback={
              <Tbody>
                {new Array(5).fill(null).map((_, index) => (
                  <Tr key={index}>
                    {new Array(4).fill(null).map((_, index) => (
                      <Td key={index}>
                        <Flex>
                          <Skeleton height="20px" width="20px" />
                        </Flex>
                      </Td>
                    ))}
                  </Tr>
                ))}
              </Tbody>
            }
          >
            <ReferralsTableBody />
          </Suspense>
        </ErrorBoundary>
      </Table>
    </TableContainer>
  )
}

function Referrals() {
  return (
    <Container maxW="full">
      <Heading size="lg" textAlign={{ base: "center", md: "left" }} pt={12}>
        Referrals Management
      </Heading>

      <Navbar type={"Referral"} />
      <ReferralsTable />
    </Container>
  )
}
