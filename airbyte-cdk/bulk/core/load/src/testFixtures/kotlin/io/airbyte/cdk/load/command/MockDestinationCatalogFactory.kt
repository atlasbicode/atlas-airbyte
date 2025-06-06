/*
 * Copyright (c) 2024 Airbyte, Inc., all rights reserved.
 */

package io.airbyte.cdk.load.command

import io.airbyte.cdk.load.data.FieldType
import io.airbyte.cdk.load.data.IntegerType
import io.airbyte.cdk.load.data.ObjectType
import io.airbyte.cdk.load.data.StringType
import io.micronaut.context.annotation.Factory
import io.micronaut.context.annotation.Primary
import io.micronaut.context.annotation.Requires
import jakarta.inject.Singleton

/**
 * Basic two-stream catalog, good for most testing purposes. Inject with
 * `@MicronautTest(environments = [ ..., MockDestinationCatalog])`.
 */
@Factory
class MockDestinationCatalogFactory : DestinationCatalogFactory {
    companion object {
        val stream1 =
            DestinationStream(
                unmappedNamespace = "test",
                unmappedName = "stream1",
                importType = Append,
                schema =
                    ObjectType(
                        properties =
                            linkedMapOf(
                                "id" to FieldType(type = IntegerType, nullable = true),
                                "name" to FieldType(type = StringType, nullable = true),
                            ),
                    ),
                generationId = 42,
                minimumGenerationId = 0,
                syncId = 42,
                namespaceMapper = NamespaceMapper()
            )
        val stream2 =
            DestinationStream(
                unmappedNamespace = "test",
                unmappedName = "stream2",
                importType = Append,
                schema =
                    ObjectType(
                        properties =
                            linkedMapOf(
                                "id" to FieldType(type = IntegerType, nullable = true),
                                "name" to FieldType(type = StringType, nullable = true),
                            ),
                    ),
                generationId = 42,
                minimumGenerationId = 0,
                syncId = 42,
                namespaceMapper = NamespaceMapper()
            )
    }

    @Singleton
    @Primary
    @Requires(env = ["MockDestinationCatalog"])
    override fun make(): DestinationCatalog {
        return DestinationCatalog(streams = listOf(stream1, stream2))
    }
}
