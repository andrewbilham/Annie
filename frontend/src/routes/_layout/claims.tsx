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
import { ClaimsService } from "../../client"
import ActionsMenu from "../../components/Common/ActionsMenu"
import Navbar from "../../components/Common/Navbar"

export const Route = createFileRoute("/_layout/claims")({
  component: Claims,
})

function ClaimsTableBody() {
  const { data: claims } = useSuspenseQuery({
    queryKey: ["claims"],
    queryFn: () => ClaimsService.readClaims({}),
  })

  return (
    <Tbody>
      {claims.data.map((claim) => (
        <Tr key={claim.id}>
          <Td>{claim.id}</Td>
          <Td>{claim.client_firstname}</Td>
          <Td color={!claim.client_lastname ? "ui.dim" : "inherit"}>
            {claim.client_lastname || "N/A"}
          </Td>
          <Td>
            <ActionsMenu type={"Claim"} value={claim} />
          </Td>
        </Tr>
      ))}
    </Tbody>
  )
}
function ClaimsTable() {
  return (
    <TableContainer>
      <Table size={{ base: "sm", md: "md" }}>
        <Thead>
          <Tr>
            <Th>ID</Th>
            <Th>Title</Th>
            <Th>Description</Th>
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
            <ClaimsTableBody />
          </Suspense>
        </ErrorBoundary>
      </Table>
    </TableContainer>
  )
}

function Claims() {
  return (
    <Container maxW="full">
      <Heading size="lg" textAlign={{ base: "center", md: "left" }} pt={12}>
        Claims Management
      </Heading>

      <Navbar type={"Claim"} />
      <ClaimsTable />
    </Container>
  )
}
