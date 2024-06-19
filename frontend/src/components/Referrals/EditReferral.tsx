import {
  Button,
  FormControl,
  FormErrorMessage,
  FormLabel,
  Input,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalFooter,
  ModalHeader,
  ModalOverlay,
} from "@chakra-ui/react"
import { useMutation, useQueryClient } from "@tanstack/react-query"
import { type SubmitHandler, useForm } from "react-hook-form"

import {
  type ApiError,
  type ReferralPublic,
  type ReferralUpdate,
  ReferralsService,
} from "../../client"
import useCustomToast from "../../hooks/useCustomToast"

interface EditReferralProps {
  referral: ReferralPublic
  isOpen: boolean
  onClose: () => void
}

const EditReferral = ({ referral, isOpen, onClose }: EditReferralProps) => {
  const queryClient = useQueryClient()
  const showToast = useCustomToast()
  const {
    register,
    handleSubmit,
    reset,
    formState: { isSubmitting, errors, isDirty },
  } = useForm<ReferralUpdate>({
    mode: "onBlur",
    criteriaMode: "all",
    defaultValues: referral,
  })

  const mutation = useMutation({
    mutationFn: (data: ReferralUpdate) =>
      ReferralsService.updateReferral({ id: referral.id, requestBody: data }),
    onSuccess: () => {
      showToast("Success!", "Referral updated successfully.", "success")
      onClose()
    },
    onError: (err: ApiError) => {
      const errDetail = (err.body as any)?.detail
      showToast("Something went wrong.", `${errDetail}`, "error")
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["referrals"] })
    },
  })

  const onSubmit: SubmitHandler<ReferralUpdate> = async (data) => {
    mutation.mutate(data)
  }

  const onCancel = () => {
    reset()
    onClose()
  }

  return (
    <>
      <Modal
        isOpen={isOpen}
        onClose={onClose}
        size={{ base: "sm", md: "md" }}
        isCentered
      >
        <ModalOverlay />
        <ModalContent as="form" onSubmit={handleSubmit(onSubmit)}>
          <ModalHeader>Edit Referral</ModalHeader>
          <ModalCloseButton />
          <ModalBody pb={6}>
            <FormControl isInvalid={!!errors.source_id}>
              <FormLabel htmlFor="source_id">Source ID</FormLabel>
              <Input
                id="source_id"
                {...register("source_id", {
                  required: "Source ID is required",
                })}
                type="text"
              />
              {errors.source_id && (
                <FormErrorMessage>{errors.source_id.message}</FormErrorMessage>
              )}
            </FormControl>
            {/* <FormControl mt={4}>
              <FormLabel htmlFor="description">Description</FormLabel>
              <Input
                id="description"
                {...register("description")}
                placeholder="Description"
                type="text"
              />
            </FormControl> */}
          </ModalBody>
          <ModalFooter gap={3}>
            <Button
              variant="primary"
              type="submit"
              isLoading={isSubmitting}
              isDisabled={!isDirty}
            >
              Save
            </Button>
            <Button onClick={onCancel}>Cancel</Button>
          </ModalFooter>
        </ModalContent>
      </Modal>
    </>
  )
}

export default EditReferral
